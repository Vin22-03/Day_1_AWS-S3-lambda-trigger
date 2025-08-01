# Real-Time File Upload Monitor Using S3 Event Triggers and AWS Lambda

 **Project Date:** 01-08-2025


---

## 📌 Problem Statement

A startup wants an automated system that detects new file uploads in their Amazon S3 bucket and responds in real-time without needing a server. Your job is to implement a serverless solution using AWS Lambda that gets triggered on file upload and logs details like file name and bucket.

---

## 🧱 Architecture

```
+--------------------------+
|      S3 Bucket           |
|  (User uploads file)     |
+-----------+--------------+
            |
            | (Event Trigger: ObjectCreated)
            v
+---------------------------+
|       AWS Lambda          |
| - Receives event payload  |
| - Extracts file details   |
| - Logs info to CloudWatch |
+---------------------------+
```

---

## ⚙️ Tools & Services Used

| AWS Service   | Purpose                                 |
|---------------|-----------------------------------------|
| S3            | File storage & event source             |
| Lambda        | Serverless backend logic                |
| CloudWatch    | Logs for monitoring Lambda execution    |
| IAM Role      | Grants permissions to Lambda function   |
| GitHub        | Version control and project showcase    |

---

## How to Test

1. Upload a file (e.g. `test.txt`) to the S3 bucket.
2. Go to AWS CloudWatch → Logs → /aws/lambda/<myS3uploadlogger>
3. Check for logs like:
   ```
   ✅ New file uploaded: test.txt to bucket: myuploadtriggerbucket1
   ```

---

## Output Example

```
✅ New file uploaded: hii my new S3 event logger.txt to bucket: myuploadtriggerbucket1
```


## What I Learned

- How to trigger Lambda from S3
- Lambda event JSON structure
- CloudWatch for real-time logging
- IAM permissions for event-driven flows

---
