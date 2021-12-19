# list-changes
A simple API to find newly added entries in a list

---

## Purpose

While trying to find new entries in a list in `JavaScript`, I couldn't find an optimal solution, array filters and other soutions simply just didn't worked out for me as I expected it to, so I build a straightforward python script to be called to find these entries!

---

## Usage

Fetch the API URL with following `payload` :

```json
{
    "old" : "encoded_old_array_string",
    "new" : "encoded_new_array_string"
}
```

Examples :

- JavaScript

    ```javascript
    async function getChanges(arr1, arr2) {
        const listChangeAPI = "https://list-changes.vercel.app/api"
        const newArr = encodeURIComponent(JSON.stringify(arr1))
        const oldArr = encodeURIComponent(JSON.stringify(arr2))
        const rawResponse = await fetch(listChangeAPI, {
            "method": "POST",
            "headers": {
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            "body": JSON.stringify({
                "old": oldArr,
                "new": newArr
            })
        });
        const changes = await rawResponse.json();
        return changes
    }
    ```

- Google App Script

    ```javascript
    function getChanges(arr1, arr2) {
        const listChangeAPI = "https://list-changes.vercel.app/api"
        const newArr = encodeURIComponent(JSON.stringify(arr1))
        const oldArr = encodeURIComponent(JSON.stringify(arr2))
        var options = {
            "method": "post",
            "payload": JSON.stringify({
            "old": oldArr,
            "new": newArr
            })
        };
        const changes = JSON.parse(UrlFetchApp.fetch(listChangeAPI, options).getContentText())
        return changes
    }
    ```

---

## License & Copyright

  - This Project is [Apache-2.0](./LICENSE) Licensed
  - Copyright 2021 [Vishal Das](https://github.com/dvishal485)