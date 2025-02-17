---
description: Pre-process and ingest diverse data formats, including images and text-based documents
sidebar_position: 2
draft: true
---

# Data Ingestion Pipelines

**Pre-process and ingest diverse data formats, including images and text-based documents**
<hr />

The [Data Ingestion Pipelines](https://github.com/Clarifai/examples/tree/main/Data_Utils/Ingestion%20pipelines) framework, part of the Data Utils library, offers a comprehensive suite of robust functions — commonly referred to as pipelines — designed to pre-process, transform, and prepare images and text documents for seamless ingestion into the Clarifai platform. 

These ready-to-use pipelines enable efficient processing of unstructured data, including partitioning, chunking, cleaning, and extracting valuable information, ensuring the data is optimized for downstream use cases such as [Retrieval Augmented Generation](https://docs.clarifai.com/portal-guide/agent-system-operators/rag-prompter) (RAG).

Leveraging the capabilities of the open-source [Unstructured](https://docs.unstructured.io/welcome) library, this framework is designed to streamline data processing workflows, making it an essential tool for working with Large Language Models (LLMs) and other AI-driven applications. 

It supports these file formats:

- PDF
- Text (.txt)
- Docx
- Markdown

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import CodeBlock from "@theme/CodeBlock";

import CreateDataset from "!!raw-loader!../../../code_snippets/python-sdk/datautils/create_dataset.py";
import PDFPartition from "!!raw-loader!../../../code_snippets/python-sdk/datautils/pdf_partition.py";
import PDFPartitionMultimodal from "!!raw-loader!../../../code_snippets/python-sdk/datautils/pdf_partition_multimodal.py";
import BuildingPipelines from "!!raw-loader!../../../code_snippets/python-sdk/datautils/building_pipelines.py";
import TextPartition from "!!raw-loader!../../../code_snippets/python-sdk/datautils/text_partition.py";
import DocxPartition from "!!raw-loader!../../../code_snippets/python-sdk/datautils/docx_partition.py";
import MarkdownPartition from "!!raw-loader!../../../code_snippets/python-sdk/datautils/markdown_partition.py";
import CleanExtraWhitespace from "!!raw-loader!../../../code_snippets/python-sdk/datautils/clean_extra_whitespace.py";
import ReplaceUnicodeQuotes from "!!raw-loader!../../../code_snippets/python-sdk/datautils/replace_unicode_quotes.py";
import CleanDashes from "!!raw-loader!../../../code_snippets/python-sdk/datautils/clean_dashes.py";
import CleanBullets from "!!raw-loader!../../../code_snippets/python-sdk/datautils/clean_bullets.py";
import GroupBrokenParagraphs from "!!raw-loader!../../../code_snippets/python-sdk/datautils/group_broken_paragraphs.py";
import RemovePunctuation from "!!raw-loader!../../../code_snippets/python-sdk/datautils/remove_punctuation.py";
import ConvertByteStrings from "!!raw-loader!../../../code_snippets/python-sdk/datautils/convert_byte_strings.py";
import CleanNonASCII from "!!raw-loader!../../../code_snippets/python-sdk/datautils/clean_non_ascii.py";
import CleanOrderedBullets from "!!raw-loader!../../../code_snippets/python-sdk/datautils/clean_ordered_bullets.py";
import CleanPrefix from "!!raw-loader!../../../code_snippets/python-sdk/datautils/clean_prefix.py";
import CleanPostfix from "!!raw-loader!../../../code_snippets/python-sdk/datautils/clean_postfix.py";

import Example1 from "!!raw-loader!../../../code_snippets/python-sdk/datautils/ingestion_example_1.txt";
import Example2 from "!!raw-loader!../../../code_snippets/python-sdk/datautils/building_pipelines_example.txt";

## Prerequisites

### Install Python SDK and Data Utils 

Install the latest version of the `clarifai` Python SDK package. Also, install the Data Utils library.

<Tabs>
<TabItem value="bash" label="Bash">
    <CodeBlock className="language-text">
    pip install --upgrade clarifai
    pip install clarifai-datautils
</CodeBlock>
</TabItem>
</Tabs>

### Install Extra Dependencies

The Data Ingestion Pipelines framework requires additional libraries to function properly. First, create a `requirements-dev.txt` file and add the following dependencies:

<Tabs>
<TabItem value="text" label="Text">
    <CodeBlock className="language-text">
    unstructured[pdf] @ git+https://github.com/clarifai/unstructured.git@support_clarifai_model
    llama-index-core==0.10.33
    llama-index-llms-clarifai==0.1.2
    pi_heif==0.18.0
    markdown==3.7
    python-docx==1.1.2
    schema==0.7.5
</CodeBlock>
</TabItem>
</Tabs>

> _Note that this command `pip install unstructured[pdf] @ git+https://github.com/clarifai/unstructured.git@support_clarifai_model` installs the `support_clarifai_model` branch from the [Clarifai fork of `unstructured`library](https://github.com/Clarifai/unstructured/tree/support_clarifai_model)._

Then, run the following command to install the required dependencies:

<Tabs>
<TabItem value="bash" label="Bash">
    <CodeBlock className="language-text">
    pip install -r requirements-dev.txt
</CodeBlock>
</TabItem>
</Tabs>

You can also install the following system dependencies if they are not already available on your system. Based on the document types you're handling, you may not need all of them.

- [`opencv-python-headless`](https://pypi.org/project/opencv-python-headless/) —  A lightweight version of OpenCV (Open Source Computer Vision Library) designed for environments where GUI functionalities (such as image or video display) are not needed. You can install it by running: `pip install opencv-python-headless`. 
- [`poppler-utils`](https://pypi.org/project/poppler-utils/) — Essential for processing and extracting data from PDF files. You can install it by running: `sudo apt update && sudo apt install poppler-utils`. 
- [`tesseract-ocr`](https://github.com/tesseract-ocr/tessdoc) — Required for performing OCR on images or scanned documents to extract text. You can install it by running: `sudo apt update && sudo apt install tesseract-ocr`. 
- [`libgl1-mesa-glx`](https://mesa3d.org/) — Ensures compatibility with graphical operations, which may be required by certain libraries (e.g., OpenCV) even in headless environments. You can install it by running: `sudo apt update && sudo apt install libgl1-mesa-glx`.
- [`punkt_tab`](https://www.nltk.org/api/nltk.tokenize.html) — Enables tokenization of text data with tab-separated values; it's part of the NLTK library. You can install it by running: `nltk.download('punkt_tab')`.
- [`averaged_perceptron_tagger_eng`](https://www.nltk.org/api/nltk.tag.html) — Provides a pre-trained model for accurate part-of-speech tagging in English; it's part of the NLTK library. You can install it by running: `nltk.download('averaged_perceptron_tagger_eng')`.  

### Get a PAT

You need a PAT (Personal Access Token) key to authenticate your connection to the Clarifai platform. You can generate it in your Personal Settings page by navigating to the [Security section](https://clarifai.com/settings/security).

Then, set it as an environment variable in your script.

<Tabs>
<TabItem value="python" label="Python">
    <CodeBlock className="language-python">
    import os
    os.environ["CLARIFAI_PAT"] = "YOUR_PAT_HERE" # replace with your own PAT key 
</CodeBlock>
</TabItem>
</Tabs>

### Create a Dataset

[Create a dataset](https://docs.clarifai.com/sdk/managing-datasets#creating-datasets) on the Clarifai platform to use for uploading your pre-processed data. 

<Tabs>
<TabItem value="python" label="Python">
    <CodeBlock className="language-python">{CreateDataset}</CodeBlock>
</TabItem>
</Tabs>

## Building Pipelines

When working with unstructured documents like PDFs, building pipelines is a crucial step to automate the processing and transformation of data. 

Here is an example of a basic pipeline for PDF partitioning. 

<Tabs>
<TabItem value="python" label="Python">
    <CodeBlock className="language-python">{BuildingPipelines}</CodeBlock>
</TabItem>
</Tabs>

<details>
  <summary>Output Example</summary>
    <CodeBlock className="language-text">{Example2}</CodeBlock>
</details> 

Note that:

- `Pipeline` and `PDFPartition` classes are imported from `clarifai_datautils.multimodal`. These are used to define and execute processing pipelines for PDF documents.
- A `Pipeline` object is created with the name `"basic_pdf"`. You can provide any arbitrary name for the pipeline. The name can be used to identify or call the pipeline. 
- `PDFPartition()` uses [default parameters](https://github.com/Clarifai/clarifai-python-datautils/blob/main/clarifai_datautils/constants/pipeline.py) (such as `max_characters=500`) for ingesting PDFs.
- After loading a predefined pipeline, you can view its details. 

## Partitioning & Chunking

[Partitioning](https://docs.unstructured.io/open-source/core-functionality/partitioning) is the first step in document processing. It breaks down a raw, unstructured document into smaller, meaningful units called document elements, while preserving the document’s semantic structure. 

These elements — such as paragraphs, titles, tables, and images — help maintain the original context. The process involves reading the document, segmenting it into sections, categorizing those sections, and extracting the relevant text.

Chunking follows partitioning and involves grouping or rearranging document elements generated by partitioning into "chunks" based on specific size constraints or criteria. This step ensures that the resulting segments are optimized for use cases like search, summarization, or content retrieval.  

:::info

Once a chunk of text or image data is uploaded to the Clarifai platform, [metadata fields](https://docs.clarifai.com/portal-guide/input-viewer/) — such as `filename`, `page_number`, `last_modified`, and `type` — are automatically added to provide detailed information about the uploaded content.

:::

### PDF Partitioning

PDF partitioning helps transform PDFs into a structured format that can be used for further processing. 

<Tabs>
<TabItem value="python" label="Python">
    <CodeBlock className="language-python">{PDFPartition}</CodeBlock>
</TabItem>
</Tabs>

<details>
  <summary>Output Example</summary>
    <CodeBlock className="language-text">{Example1}</CodeBlock>
</details> 

Note that:

- The transformation step uses the `PDFPartition` object to partition the PDF into smaller chunks. 
    - `chunking_strategy` is set to `"by_title"`, meaning the document is split based on its title sections.
    - `max_characters` limits each chunk to 1024 characters for better processing and retrieval efficiency. The default behavior is 500 characters. 
- The `loader=False`, which is the default, argument ensures the transformed chunks are returned as Python objects (`elements`), allowing for local inspection or further processing. Conversely, setting `loader=True` directly ingests the transformed chunks into a Clarifai dataset instead of just returning them locally.
- The partitioned and chunked PDF elements are uploaded to a Clarifai dataset. The uploaded data is automatically [annotated](https://docs.clarifai.com/portal-guide/input-viewer/) with the pipeline name on the Clarifai platform. This makes it easy to identify and distinguish between data processed through different pipelines.


:::note tips

You can also configure the following arguments for the `PDFPartition` object:

    - Set `chunking_strategy="basic"` for the document to be chunked purely based on character length and sequential order rather than structural elements like section titles or page boundaries. It's useful when you simply want to group text into evenly sized chunks without preserving the document’s logical structure. _Note that if you do not set the chunking strategy, either by `by_title` or `basic`, no chunking is performed._
    - Set `ocr=True` to enable OCR for extracting text from scanned or image-based PDFs. Set it to `False`, which is the default, to disable OCR. 
    - By default, `overlap=None` or `overlap=0`  ensures no overlap between chunks; that is, chunks are created without any shared text between them. To enable overlap, provide an integer value (e.g., `overlap=100`) to specify the number of overlapping characters between consecutive chunks.
    - Set `overlap_all=True` to enable overlapping across all chunks. Set it to `False`, which is the default, to disable this behavior.
    - Set `strategy="ocr_only"` to force the document to be processed using the Tesseract OCR strategy. If Tesseract is unavailable and the document contains extractable text, it falls back to the `"fast"` strategy. Set `strategy="fast"` to extract text using `pdfminer`, which is faster and suitable for text-based PDFs. Otherwise, `strategy="auto"` is the default that selects the partitioning strategy based on document characteristics and the function kwargs. 
    - Use `clarifai_ocr_model` to set the URL of a Clarifai OCR model for processing the document. The default is `None`. 

:::

### PDF Partitioning Multimodal

The `PDFPartitionMultimodal` ingestion pipeline supports multimodal scenarios, where files containing a mix of text, images, and other elements are to be processed and ingested into the Clarifai platform.

We use the Clarifai-hosted YOLOX object detection model to process the PDFs containing embedded images.

<Tabs>
<TabItem value="python" label="Python">
    <CodeBlock className="language-python">{PDFPartitionMultimodal}</CodeBlock>
</TabItem>
</Tabs>

Note that:

- The`PDFPartitionMultimodal` supports the following arguments for configuration: `chunking_strategy`, `max_characters`, `overlap`, and `overlap_all`, which have been explained earlier.

:::note tips

You can also configure the following arguments for the `PDFPartitionMultimodal` object:

    - By default, `extract_images_in_pdf=True` extracts images from a PDF file. In that case, the partitioning strategy is set as `strategy="hi_res"`, which is intended to identify the layout of the document and gain additional information about the document elements. Otherwise, set `extract_images_in_pdf=False` to disable this behavior.
    - Set `extract_image_block_types=["Image"]` to specify that you want to extract a list of image block types.
    - Set `extract_image_block_to_payload=True` to allow for the conversion of extracted images from a PDF into base64 format (return images as bytes). Note that to use this feature, you must set the `strategy` parameter to `hi_res` and `extract_images_in_pdf` to `True`. Otherwise, set `extract_image_block_to_payload=False` to disable this behavior.
    
:::

### Text Partitioning

Text partitioning transforms unstructured `.txt` documents into text elements, making them easier to process, analyze, and utilize in downstream applications.

<Tabs>
<TabItem value="python" label="Python">
    <CodeBlock className="language-python">{TextPartition}</CodeBlock>
</TabItem>
</Tabs>

Note that:

- The `TextPartition` object supports the following arguments for configuration:  `chunking_strategy`, `max_characters`, `overlap`, and `overlap_all`, which have been explained earlier.

### Docx Partitioning

Docx partitioning processes `.docx` files, extracting and partitioning their contents into structured text elements. 

<Tabs>
<TabItem value="python" label="Python">
    <CodeBlock className="language-python">{DocxPartition}</CodeBlock>
</TabItem>
</Tabs>

Note that:

- The `DocxPartition` object supports the following arguments for configuration:  `chunking_strategy`, `max_characters`, `overlap`, and `overlap_all`, which have been explained earlier.

### Markdown Partitioning

Markdown partitioning processes `.md` files, breaking them down into structured text elements for improved usability in downstream applications. 

<Tabs>
<TabItem value="python" label="Python">
    <CodeBlock className="language-python">{MarkdownPartition}</CodeBlock>
</TabItem>
</Tabs>

Note that:

- The `MarkdownPartition` object supports the following arguments for configuration:  `chunking_strategy`, `max_characters`, `overlap`, and `overlap_all`, which have been explained earlier.

## Text Cleaning

The Data Ingestion Pipelines framework allows you to prepare and refine raw text data by removing or correcting unwanted elements to improve readability, consistency, and usability for downstream applications. 

:::note

The following examples use the `PDFPartition` object, but they can also be applied to any other supported partitioning objects.

:::

### Clean Extra Whitespaces

You can remove unnecessary spaces, tabs, or newlines from documents. 

<Tabs>
<TabItem value="python" label="Python">
    <CodeBlock className="language-python">{CleanExtraWhitespace}</CodeBlock>
</TabItem>
</Tabs>

### Replace Unicode Quotes

You can replace Unicode quotes with ASCII quotes for standardization.

<Tabs>
<TabItem value="python" label="Python">
    <CodeBlock className="language-python">{ReplaceUnicodeQuotes}</CodeBlock>
</TabItem>
</Tabs>

### Clean Dashes

You can remove unnecessary dashes from texts.  

<Tabs>
<TabItem value="python" label="Python">
    <CodeBlock className="language-python">{CleanDashes}</CodeBlock>
</TabItem>
</Tabs>

### Clean Bullets

You can remove unnecessary bullets from texts.  

<Tabs>
<TabItem value="python" label="Python">
    <CodeBlock className="language-python">{CleanBullets}</CodeBlock>
</TabItem>
</Tabs>


### Group Broken Paragraphs

You can merge fragmented paragraphs that were unintentionally split, restoring proper text flow and improving readability.  

<Tabs>
<TabItem value="python" label="Python">
    <CodeBlock className="language-python">{GroupBrokenParagraphs}</CodeBlock>
</TabItem>
</Tabs>

### Remove Punctuations

You can remove unnecessary punctuations from texts.  

<Tabs>
<TabItem value="python" label="Python">
    <CodeBlock className="language-python">{RemovePunctuation}</CodeBlock>
</TabItem>
</Tabs>

### Convert Byte Strings

You can convert a byte string (such as `b'hello'`) into a regular string (`'hello'`), ensuring proper text formatting and usability.

<Tabs>
<TabItem value="python" label="Python">
    <CodeBlock className="language-python">{ConvertByteStrings}</CodeBlock>
</TabItem>
</Tabs>

### Clean Non-ASCII Characters 

You can remove non-ASCII characters from text, ensuring compatibility with systems that only support standard ASCII encoding.

<Tabs>
<TabItem value="python" label="Python">
    <CodeBlock className="language-python">{CleanNonASCII}</CodeBlock>
</TabItem>
</Tabs>

### Clean Ordered Bullets

You can remove ordered bullet points(such as `1.`, `2)`, or `III.`) from text.

<Tabs>
<TabItem value="python" label="Python">
    <CodeBlock className="language-python">{CleanOrderedBullets}</CodeBlock>
</TabItem>
</Tabs>

### Clean Prefix

You can remove a specified prefix from a document. The `Clean_prefix` object supports the following arguments:

- `pattern` — Defines the prefix to remove. The pattern must be provided, and it can be a simple string or a regex pattern.
- `ignore_case` (optional, default is `False`) — Determines whether to ignore case. If `True`, ensures case-insensitive matching.
- `strip` (optional, default is `True`) — If `True`, removes any leading whitespace after the prefix is removed.

<Tabs>
<TabItem value="python" label="Python">
    <CodeBlock className="language-python">{CleanPrefix}</CodeBlock>
</TabItem>
</Tabs>

### Clean Postfix

You can remove a specified postfix from a document using the `Clean_postfix` object, which supports the same arguments as `Clean_prefix`.

<Tabs>
<TabItem value="python" label="Python">
    <CodeBlock className="language-python">{CleanPostfix}</CodeBlock>
</TabItem>
</Tabs>

## Text Extraction

