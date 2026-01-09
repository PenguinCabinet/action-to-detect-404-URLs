# action-to-detect-404-URLs

これはリポジトリ内のURLを抽出し、指定されたステータスコードのURLを検知するGithub Actionsです。     
リンク切れのURLを検知する使い方を想定しています。

This is a Github Action that extracts URLs in a repository and detects URLs with a specified status code.   
It is intended to be used to detect broken URLs.

## Usage

```yaml
on:
  push:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: test
        uses: PenguinCabinet/action-to-detect-404-URLs@v0.0.1
        with:
          working_directory: "./"
          filter_mode: "deny" #"allow" mode or "deny" mode
          filter_status_code: "4.." #Detects URLs with status codes in the 400 range. Can be written using regular expressions.
          detect_URLs_that_cannot_connect_to_the_server: true
          wait_time: 1
```

