query = """
WITH all_pipeline AS ( SELECT dag_id, subdag_id,
       Json_agg(pipeline) dag_flow 
FROM   (
        SELECT dag_id, subdag_id,
               Row_to_json(bq_to_bq_config) pipeline 
        FROM   (SELECT
                    bq_to_bq.*,
                    md.retry_delay
                FROM bq_to_bq
                JOIN main_dag md on bq_to_bq.dag_id = md.dag_id
                WHERE bq_to_bq.enabled = true and bq_to_bq.dag_id = {dag_id}
        ) bq_to_bq_config
        
        UNION ALL 
        
        SELECT dag_id, subdag_id,
               Row_to_json(bq_to_gs_config) pipeline 
        FROM   (SELECT 
                    bq_to_gs.*,
                    md.retry_delay
                FROM bq_to_gs
                JOIN main_dag md on bq_to_gs.dag_id = md.dag_id
                WHERE bq_to_gs.enabled = true AND bq_to_gs.dag_id = {dag_id}
        ) bq_to_gs_config
        
        UNION ALL 
        
        SELECT dag_id, subdag_id, Row_to_json(bq_to_bt_config) pipeline 
        FROM   (SELECT 
                    df.df_project_id, 
                    df.df_runner, 
                    df.df_staging_location, 
                    df.df_temp_location, 
                    df.df_temp_dataset,
                    df.df_network, 
                    df.df_sub_network, 
                    df.df_region, 
                    df.df_zone, 
                    df.df_worker_machine_type, 
                    df.df_worker_disk_type, 
                    df.df_disk_size_gb, 
                    df.df_service_account, 
                    
                    bt_jobs.id,
                    bt_jobs.max_numb_worker, 
                    bt_jobs.task_name, 
                    bt_jobs.bt_instance_id, 
                    bt_jobs.bigtable_id, 
                    replace(bt_jobs.sql_query::text, '"', '\\"') as sql_query,
                    replace(bt_jobs.row_keys_builder::text, '"', '\\"') as row_keys_builder,
                    replace(bt_jobs.cf_mapping::text, '"', '\\"') as cf_mapping,
                    bt_jobs.dag_id, 
                    bt_jobs.subdag_id,
                    bt_jobs.dependency,
                    bt_jobs.wait_for,
                    bt_jobs.class_name,
                    bt_jobs.protobuf_file::text as protobuf_file,
                    bt_jobs.protobuf_mapping,
                    bt_jobs.bt_project_id,
                    bt_jobs.interactive_query,
                    bt_jobs.rate_limiter,
                    replace(bt_jobs.dataflow_labels::text, '"', '\\"') as dataflow_labels,
                    md.retry_delay
                FROM bq_to_bt bt_jobs 
                LEFT JOIN dataflow_config df ON bt_jobs.df_id = df.df_id 
                JOIN main_dag md on bt_jobs.dag_id = md.dag_id
                WHERE bt_jobs.enabled = true 
                AND bt_jobs.dag_id = {dag_id}
        ) bq_to_bt_config
        
        UNION ALL
        
        SELECT dag_id, subdag_id, Row_to_json(bq_to_slave_config) pipeline 
        FROM   (SELECT 
                    df.df_project_id, 
                    df.df_runner, 
                    df.df_staging_location, 
                    df.df_temp_location, 
                    df.df_temp_dataset,
                    df.df_network,
                    df.df_sub_network, 
                    df.df_region, 
                    df.df_zone, 
                    df.df_worker_machine_type, 
                    df.df_worker_disk_type, 
                    df.df_disk_size_gb, 
                    df.df_service_account, 
                    
                    bqs_jobs.id,
                    bqs_jobs.dag_id,
                    bqs_jobs.task_name,
                    bqs_jobs.max_numb_worker,
                    bqs_jobs.dependency,
                    bqs_jobs.wait_for,
                    bqs_jobs.subdag_id,
                    bqs_jobs.destination_table_name,
                    bqs_jobs.destination_table_schema::text as destination_table_schema,
                    replace(bqs_jobs.source_sql_query::text, '"', '\\"') source_sql_query,
                    bqs_jobs.interactive_query,
                    dc.db_id,
                    dc.db_name,
                    dc.db_type,
                    dc.db_username,
                    dc.db_password,
                    dc.db_host,
                    dc.db_port,
                    dc.db_param_str,
                    md.retry_delay
                    
                FROM bq_to_slave bqs_jobs 
                LEFT JOIN dataflow_config df ON bqs_jobs.df_id = df.df_id
                LEFT JOIN database_connection dc ON bqs_jobs.db_id = dc.db_id
                JOIN main_dag md on bqs_jobs.dag_id = md.dag_id
                WHERE  bqs_jobs.enabled = true 
                AND bqs_jobs.dag_id = {dag_id}
        ) bq_to_slave_config
        
        UNION ALL 
        
        SELECT dag_id, subdag_id, Row_to_json(spark_cf) pipeline 
          FROM   ( 
            SELECT
                dag_id, subdag_id, task_name, submit_type, file, proxy_user, class_name, args, jars, py_files, files, 
                driver_memory, driver_cores, executor_memory, executor_cores, num_executors, archives, queue, 
                session_name, conf, dependency, wait_for, livy_host, file_dir, requirement_txt, python_version, 
                final_machine_state, df_runner as machine_name, df_network as machine_network, 
                df_region as machine_region, df_zone as machine_zone,
                df_sub_network as machine_subnet, df_worker_machine_type as machine_type
            FROM
                spark_config
            LEFT JOIN dataflow_config ON machine_type_id = df_id
            WHERE  enabled = true and dag_id = {dag_id}) spark_cf 
        
        UNION ALL 
        
        SELECT dag_id, subdag_id, Row_to_json(bq_to_pubsub_config) pipeline 
        FROM   (SELECT 
                    df.df_project_id, 
                    df.df_runner, 
                    df.df_staging_location, 
                    df.df_temp_location,
                    df.df_temp_dataset,
                    df.df_network, 
                    df.df_sub_network, 
                    df.df_region, 
                    df.df_zone, 
                    df.df_worker_machine_type, 
                    df.df_worker_disk_type, 
                    df.df_disk_size_gb, 
                    df.df_service_account, 
                    
                    pub_jobs.id,
                    pub_jobs.max_numb_worker, 
                    pub_jobs.task_name, 
                    replace(pub_jobs.sql_query::text, '"', '\\"') as sql_query,
                    pub_jobs.dag_id, 
                    pub_jobs.subdag_id,
                    pub_jobs.dependency,
                    pub_jobs.wait_for,
                    pub_jobs.target_topics,
                    pub_jobs.interactive_query,
                    md.retry_delay
                FROM bq_to_pubsub pub_jobs 
                LEFT JOIN dataflow_config df ON pub_jobs.df_id = df.df_id 
                JOIN main_dag md on pub_jobs.dag_id = md.dag_id
                WHERE  pub_jobs.enabled = true 
                AND pub_jobs.dag_id = {dag_id}
        ) bq_to_pubsub_config 
        
        UNION ALL
        
        SELECT dag_id, subdag_id,
               Row_to_json(gs_to_bq_config) pipeline 
        FROM   (SELECT 
                    gs_to_bq.*,
                    md.retry_delay
                FROM gs_to_bq
                JOIN main_dag md on gs_to_bq.dag_id = md.dag_id
                WHERE gs_to_bq.enabled = true and gs_to_bq.dag_id = {dag_id}
        ) gs_to_bq_config 
        
        UNION ALL
        
        SELECT dag_id, subdag_id,
               Row_to_json(http_request_config) pipeline 
        FROM   (SELECT 
                    http_request.*,
                    md.retry_delay
                FROM http_request
                JOIN main_dag md ON http_request.dag_id = md.dag_id
                WHERE http_request.enabled = true AND http_request.dag_id = {dag_id}
        ) http_request_config
    ) AS all_pipeline
GROUP BY dag_id, subdag_id )
SELECT 
    all_pipeline.dag_id,
    main_dag.dag_name,
    all_pipeline.subdag_id,
    s.subdag_name,
    dag_flow,
    s.sla_in_minutes,
    main_dag.description,
    s.dependency,
    s.priority_weight,
    s.wait_for,
    s.wait_for_fixed_time,
    s.slack_webhook,
    s.queue_name,
    s.sa_conn_id,
    s.success_slack_webhook,
    main_dag.retry_delay
FROM all_pipeline
INNER JOIN main_dag ON all_pipeline.dag_id = main_dag.dag_id
LEFT JOIN sub_dag s ON all_pipeline.subdag_id = s.subdag_id;
"""