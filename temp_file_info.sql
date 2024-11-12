--Query temporary file information
SELECT
 f.file_id,
 f.file_name,
 f.file_type,
 f.tablespace_name,
 f.create_date AS created_time
FROM dba_temp_files f;
