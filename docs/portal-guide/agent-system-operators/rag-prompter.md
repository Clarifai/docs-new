---
description: Learn how to enhance the quality and relevance of LLM-generated text
sidebar_position: 1.1
---

# RAG Prompter

**Learn how to enhance the quality and relevance of LLM-generated text**
<hr />

The RAG Prompter is a prompt template operator that leverages the [Retrieval-Augmented Generation (RAG)](https://www.clarifai.com/blog/what-is-rag-retrieval-augmented-generation) technique to improve the performance of Large Language Models (LLMs). 

LLMs have revolutionized natural language understanding across various applications and industries. These models have introduced a new era of quick problem-solving and AI-powered interactions. 

However, LLMs are often plagued by these two main limitations:

- Most traditional LLMs have a static knowledge base that is limited to a specific period; for example, as of this writing, ChatGPT's knowledge cut-off is in October 2023. This makes them outdated and unable to respond accurately to recent events. 

- Most traditional LLMs are trained on an extensive, generalized collection of data, which may not be applicable to your specific use case. Whenever LLMs confront voids in their training data, they might generate seemingly plausible yet erroneous information, a phenomenon referred to as "hallucination."

RAG helps solve these issues by incorporating your data into the existing dataset that is accessible to LLMs. With the RAG AI framework, you can retrieve facts from an external knowledge base, thereby anchoring LLMs with the most precise and current information available. 

Additionally, RAG reduces the necessity for users to continuously train a model on new data and update its parameters to accommodate evolving circumstances. RAG allows users to do much cheaper in-context learning and reduces the need for expensive LLM fine-tuning.

:::note

- The RAG Prompter model type should not be set as an app’s [base workflow]( https://docs.clarifai.com/portal-guide/workflows/base-workflows/); otherwise, it would cause a dependency cycle.

- This model generates search billable events. 

:::

## How RAG Works 

As its name implies, RAG works through two phases: retrieval and content generation. 

When a user uploads external data to be used for RAG purposes into a Clarifai application, the data is first chunked into bite-sized pieces. The chunks are then passed through an embedding model, which transforms the data into indexed vectors and stores them in a vector database. 

:::info

[Embedding models](https://docs.clarifai.com/api-guide/predict/embeddings) are the type of models usually used to convert data into numerical vectors, while preserving meaningful relationships between them. These vectors are like condensed summaries of the data, capturing its important aspects in a way that machine learning models can understand. By using these vectors, the models can now reason about the data, compare different pieces of information, and perform tasks like similarity search. 

:::

When an LLM is asked a question, the prompt will first pass through an embedding model and also be converted into a vector. Algorithms will search the Clarifai vector store to *retrieve* the chunks most relevant to that provided user’s prompt. 

The most relevant chunks are then appended to the user’s query and served as context – extending the prompt to the LLM with a lot of background information. 

Next, in the generative phase, the LLM leverages the *augmented* prompt along with its internal representation of training data to craft a compelling response tailored to the user's query at that moment.

![](https://www.clarifai.com/hs-fs/hubfs/rag-query-drawio%20(1)-png-2.png?width=2056&height=1334&name=rag-query-drawio%20(1)-png-2.png)

Image source: [Clarifai portal](https://www.clarifai.com/hs-fs/hubfs/rag-query-drawio%20(1)-png-2.png?width=2056&height=1334&name=rag-query-drawio%20(1)-png-2.png)

## How to Create a RAG Prompter

Let’s demonstrate how you can create a RAG Prompter model on the Clarifai platform. 

:::note objective

Our intention is to search an app containing textual data for relevant information related to a provided text query. We extract the top k most relevant results from the app, and augment these results into the prompt we provide to the model. By leveraging the additional context, the model should be able to generate a more informative response to the question. 

:::

### Step 1: Create an Application

[Click here](https://docs.clarifai.com/clarifai-basics/applications/create-an-application/#create-an-application-on-the-portal) to learn how to create an application on the Clarifai portal.

:::info Base Workflow

When creating the application, select the **Text/Document** option as the primary input type. And in the collapsible **Advanced Settings** field, select an embeddings workflow, such as the [baai-general-embedding-base-en](https://clarifai.com/clarifai/main/workflows/baai-general-embedding-base-en) as the [base workflow](https://docs.clarifai.com/portal-guide/workflows/base-workflows/). The base workflow will convert the uploaded data into indexed vectors, which makes them searchable – as explained earlier. 

:::

###  Step 2: Upload Data

Next, upload the external data you want to use to optimize the output of a large language model. [Click here](https://docs.clarifai.com/portal-guide/inputs-manager/upload-inputs) to learn how you can upload data to your application. 

You can also [create a dataset](https://docs.clarifai.com/portal-guide/datasets/create-get-update-delete/#create-datasets) and add your inputs to it, then specify the dataset ID when configuring the RAG Prompter. This ensures the RAG Prompter performs context-based searches within the specified dataset, which leads to more accurate and relevant outputs.  

If a dataset ID is not specified, the RAG Prompter will search across all inputs in your app, spanning all datasets. This can result in mixed context searches and less precise outputs due to jumbled context hits from unrelated datasets.

Similarly, you can attach JSON metadata to your inputs when uploading them to the Clarifai platform. Metadata serve as additional information associated with your inputs and, like dataset IDs, can be used to narrow down search results. By specifying metadata, you can filter search results to match specific conditions, which further improves the relevance and accuracy of the context provided by the RAG Prompter.

:::warning RAG in four lines of code

[Click here]( https://www.clarifai.com/blog/retrieval-augmented-generation-rag-in-4-lines-of-code) to learn how to build a RAG system in four lines of code. You’ll also learn how to upload documents seamlessly to your Clarifai application. 

:::

For this example, let's add the following inputs to a dataset in our app:

```
The audit findings indicate that $460,000 was expended on machinery repairs during the previous twelve months. 
```

```
The total expenditure allocated to machinery repairs in the 2022 fiscal year amounted to $500,000. 
```

```
The expenses for machinery repairs in the year 2021 totaled $550,000, reflecting increased maintenance requirements.
```

```
The financial records indicate that $480,000 was disbursed for machinery repairs during 2020 calendar year.
```

```
During the 2019 fiscal year, the organization disbursed $475,000 on machinery repairs to ensure operational efficiency. 
``` 

###  Step 3: Create a Workflow

Go to the [workflow builder](https://docs.clarifai.com/portal-guide/workflows/workflow-builder/). 

Then, search for the **rag-prompter** node in the left-hand sidebar and drag it onto the empty workspace. 

![](/img/others/rag-prompter-1.png)

Use the pop-up that appears on the right-hand sidebar to set up the template text as a single-line statement. For this example, let's use this prompt template text:

```
Context information is below: {data.hits} Given the context information and not prior knowledge, answer the query.Query: {data.text.raw} Answer: 
```

:::tip

Your prompt template must include at least one instance of each of these placeholders: `{data.text.raw}` and `{data.hits}`. During inference, all instances of `{data.text.raw}` within the template will be substituted with the user query provided. Similarly, `{data.hits}` will represent a newline-separated list of search results retrieved from your app’s data and ordered by similarity.

:::

To customize your search experience, you can:

- Adjust the `min_score` parameter if you desire a minimum threshold for search result scores.

- Modify `max_results` to specify the maximum number of relevant search results included in the prompt.

- Provide a comma-separated list of `dataset_ids` or a single dataset ID for the RAG Prompter to search within. This ensures the search results are confined to specific datasets, which improves relevance and precision, as earlier explained.  

- Define the `metadata` in JSON format to filter the search results further. Just like specifying a dataset ID, using [metadata](https://docs.clarifai.com/portal-guide/psearch/pfilter/#filter-by-metadata) enhances context generation and boosts the accuracy of the results. 

To finalize creating your workflow, connect the **rag-prompter** to a text-to-text node, and choose a text-to-text LLM from the Clarifai Community, such as [GPT-4 Turbo](https://clarifai.com/openai/chat-completion/models/gpt-4-turbo).

Then, click the **Save Workflow** button to save your workflow.

### Step 4: Use the Workflow

After saving the workflow, you’ll be directed to its individual page, where you can start using it. 

Click the **+** button to provide your query text.

For example, you could provide the following as your input text:

```
How much was spent on machinery repairs in 2020?
```

Click the **Submit** button.

Once the workflow has completed processing your input, you'll see the results, starting with the earlier template text, now adapted to your input.

As you can see below, the LLM model leveraged the additional context to generate an accurate response to the question. 

![](/img/others/rag-prompter-2.png)

## How to Edit a RAG Prompter

After creating your RAG Prompter, you can edit it by navigating to its individual page and clicking the **Edit workflow** button in the upper-right section.

![](/img/others/rag-prompter-3.png)

You'll be redirected to the workflow editor page, where you can make any changes needed, such as updating the prompt template text or other parameters. 

![](/img/others/rag-prompter-4.png)

Once you've made your changes, click the **Save as new version** button to save the updated RAG Prompter under a new version — without exiting the workflow editor. 

:::note

You can easily switch between different versions of the RAG Prompter by selecting the respective version ID from the left sidebar in the workflow editor.

:::

Note that clicking the **Update Workflow** button creates a new version of your RAG Prompter and exits the workflow editor, redirecting you to its main page.

You can then select the version to use for inferencing. 

![](/img/others/rag-prompter-5.png)

<!--
:::note

You can try this workflow [here](https://clarifai.com/clarifai/Sample-Workflows-for-Docs/workflows/RAG-Prompter?version=0d6fdf0f67df4dbfa386ff8c76a3cb77). 

:::
-->