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
        uses: PenguinCabinet/action-to-detect-404-URLs@main
        with:
          working_directory: "./" # The directory path to check
          filter_mode: "deny" # "allow" mode or "deny" mode
          filter_status_code: "4.." # Detects URLs with status codes in the 400 range. Can be written using regular expressions.
          detect_URLs_that_cannot_connect_to_the_server: true # Whether to detect when the server cannot be connected
          wait_time: 1 # Request sending interval(second)
```
### Example output
```
Did not pass. There are detected URLs.
http://example.example,-1
http://example.com/404_TEST_TEST,404
Error: Process completed with exit code 255.
```
サーバーに接続できなかった場合、-1が出力されます。

-1 is output if the server could not be contacted.
