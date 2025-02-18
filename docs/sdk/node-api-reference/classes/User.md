[clarifai-nodejs](../README.mdx) / [Exports](../modules.md) / User 

# Class: User

User is a class that provides access to Clarifai API endpoints related to user information.

## Hierarchy

- `Lister`

  ↳ **`User`**

## Table of contents

### Constructors

- [constructor](User.md#constructor)

### Methods

- [app](User.md#app)
- [createApp](User.md#createapp)
- [createRunner](User.md#createrunner)
- [deleteApp](User.md#deleteapp)
- [deleteRunner](User.md#deleterunner)
- [listApps](User.md#listapps)
- [listRunners](User.md#listrunners)
- [runner](User.md#runner)

## Constructors

### constructor

• **new User**(`authConfig?`): [`User`](User.md)

Initializes an User object with the specified authentication configuration.

### Example
```ts
import { User } from "clarifai-nodejs";

export const user = new User({
  pat: process.env.CLARIFAI_PAT!,
  userId: process.env.CLARIFAI_USER_ID!,
  appId: process.env.CLARIFAI_APP_ID!,
});
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `authConfig` | `AuthConfig` | An object containing the authentication configuration. Defaults to an empty object. |

#### Returns

[`User`](User.md)

#### Overrides

Lister.constructor

#### Defined in

[client/user.ts:51](https://github.com/Clarifai/clarifai-nodejs/blob/4511094/src/client/user.ts#L51)

## Methods

### app

▸ **app**(`appId`): `Promise`\<`undefined` \| `AsObject`\>

Returns an App object for the specified app ID.

### Example
```ts
import { User } from "clarifai-nodejs";

export const user = new User({
  pat: process.env.CLARIFAI_PAT!,
  userId: process.env.CLARIFAI_USER_ID!,
  appId: process.env.CLARIFAI_APP_ID!,
});
const app = await user.app({
  appId: "app_id",
});
console.log(app);
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `appId` | `Object` | The app ID for the app to interact with. |
| `appId.appId` | `string` | - |

#### Returns

`Promise`\<`undefined` \| `AsObject`\>

An App object for the specified app ID.

#### Defined in

[client/user.ts:236](https://github.com/Clarifai/clarifai-nodejs/blob/4511094/src/client/user.ts#L236)

___

### createApp

▸ **createApp**(`«destructured»`): `Promise`\<`AsObject`\>

Creates an app for the user.

### Example
```ts
import { User } from "clarifai-nodejs";

export const user = new User({
  pat: process.env.CLARIFAI_PAT!,
  userId: process.env.CLARIFAI_USER_ID!,
  appId: process.env.CLARIFAI_APP_ID!,
});
const app = await user.createApp({
  appId: "app_id",
  baseWorkflow: "Universal",
});
console.log(app);
```

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `«destructured»` | `Object` | `undefined` |
| › `appId` | `string` | `undefined` |
| › `baseWorkflow?` | `string` | `"Empty"` |

#### Returns

`Promise`\<`AsObject`\>

An App object for the specified app ID.

#### Defined in

[client/user.ts:143](https://github.com/Clarifai/clarifai-nodejs/blob/4511094/src/client/user.ts#L143)

___

### createRunner

▸ **createRunner**(`«destructured»`): `Promise`\<`AsObject`\>

Creates a runner for the user.

### Example
```ts
import { User } from "clarifai-nodejs";

export const user = new User({
  pat: process.env.CLARIFAI_PAT!,
  userId: process.env.CLARIFAI_USER_ID!,
  appId: process.env.CLARIFAI_APP_ID!,
});
const runner = await user.createRunner({
  runnerId: "runner_id",
  labels: ["label to link runner"],
  description: "laptop runner",
});
console.log(runner);
```

#### Parameters

| Name | Type |
| :------ | :------ |
| `«destructured»` | `Object` |
| › `description` | `string` |
| › `labels` | `string`[] |
| › `runnerId` | `string` |

#### Returns

`Promise`\<`AsObject`\>

A runner object for the specified Runner ID.

#### Defined in

[client/user.ts:191](https://github.com/Clarifai/clarifai-nodejs/blob/4511094/src/client/user.ts#L191)

___

### deleteApp

▸ **deleteApp**(`appId`): `Promise`\<`void`\>

Deletes an app for the user.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `appId` | `Object` | The app ID for the app to delete. |
| `appId.appId` | `string` | - |

#### Returns

`Promise`\<`void`\>

**`Example`**

```ts
examples/user/deleteApp.ts
```

#### Defined in

[client/user.ts:294](https://github.com/Clarifai/clarifai-nodejs/blob/4511094/src/client/user.ts#L294)

___

### deleteRunner

▸ **deleteRunner**(`runnerId`): `Promise`\<`void`\>

Deletes a runner for the user.

### Example
```ts
import { User } from "clarifai-nodejs";

export const user = new User({
  pat: process.env.CLARIFAI_PAT!,
  userId: process.env.CLARIFAI_USER_ID!,
  appId: process.env.CLARIFAI_APP_ID!,
});
await user.deleteRunner({ runnerId: "runner_id" });
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `runnerId` | `Object` | The runner ID to delete. |
| `runnerId.runnerId` | `string` | - |

#### Returns

`Promise`\<`void`\>

#### Defined in

[client/user.ts:319](https://github.com/Clarifai/clarifai-nodejs/blob/4511094/src/client/user.ts#L319)

___

### listApps

▸ **listApps**(`«destructured»?`): `AsyncGenerator`\<`AsObject`[], `void`, `unknown`\>

Lists all the apps for the user.

### Example
```ts
import { User } from "clarifai-nodejs";

export const user = new User({
  pat: process.env.CLARIFAI_PAT!,
  userId: process.env.CLARIFAI_USER_ID!,
  appId: process.env.CLARIFAI_APP_ID!,
});
const list = await user
  .listApps({
    pageNo: 1,
    perPage: 20,
    params: {
      sortAscending: true,
    },
  })
  .next();
const apps = list.value;
console.log(apps);
```

#### Parameters

| Name | Type |
| :------ | :------ |
| `«destructured»` | `Object` |
| › `pageNo?` | `number` |
| › `params?` | [`ListAppsRequestParams`](../modules.md#listappsrequestparams) |
| › `perPage?` | `number` |

#### Returns

`AsyncGenerator`\<`AsObject`[], `void`, `unknown`\>

**`Yields`**

App objects for the user.

**`Note`**

Defaults to 16 per page if pageNo is specified and perPage is not specified.
If both pageNo and perPage are None, then lists all the resources.

#### Defined in

[client/user.ts:68](https://github.com/Clarifai/clarifai-nodejs/blob/4511094/src/client/user.ts#L68)

___

### listRunners

▸ **listRunners**(`«destructured»?`): `AsyncGenerator`\<`AsObject`, `void`, `unknown`\>

Lists all the runners for the user.

### Example
```ts
import { User } from "clarifai-nodejs";

export const user = new User({
  pat: process.env.CLARIFAI_PAT!,
  userId: process.env.CLARIFAI_USER_ID!,
  appId: process.env.CLARIFAI_APP_ID!,
});
const list = await user.listRunners().next();
const runners = list.value;
console.log(runners);
```

#### Parameters

| Name | Type |
| :------ | :------ |
| `«destructured»` | `Object` |
| › `pageNo?` | `number` |
| › `params?` | [`ListRunnersRequestParams`](../modules.md#listrunnersrequestparams) |
| › `perPage?` | `number` |

#### Returns

`AsyncGenerator`\<`AsObject`, `void`, `unknown`\>

**`Yields`**

Runner objects for the user.

**`Note`**

Defaults to 16 per page if perPage is not specified.

#### Defined in

[client/user.ts:109](https://github.com/Clarifai/clarifai-nodejs/blob/4511094/src/client/user.ts#L109)

___

### runner

▸ **runner**(`runnerId`): `Promise`\<`undefined` \| `AsObject`\>

Returns a Runner object if exists.

### Example
```ts
import { User } from "clarifai-nodejs";

export const user = new User({
  pat: process.env.CLARIFAI_PAT!,
  userId: process.env.CLARIFAI_USER_ID!,
  appId: process.env.CLARIFAI_APP_ID!,
});
const runner = await user.runner({ runnerId: "runner_id" });
console.log(runner);
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `runnerId` | `Object` | The runner ID to interact with. |
| `runnerId.runnerId` | `string` | - |

#### Returns

`Promise`\<`undefined` \| `AsObject`\>

A Runner object for the existing runner ID.

#### Defined in

[client/user.ts:265](https://github.com/Clarifai/clarifai-nodejs/blob/4511094/src/client/user.ts#L265)
