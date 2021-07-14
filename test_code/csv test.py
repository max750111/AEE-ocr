import csv
with open('output.csv', newline='') as csvfile:

  # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
  rows = csv.DictReader(csvfile)

  # 以迴圈輸出指定欄位
  for row in rows:
    print(row['filename'], row['string'])
