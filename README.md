Nvidia-docker is needed

Usage:

1. To run generation   
```python run.py path_to_content_image path_to_style_image path_to_dir_store_result```

1. Build an image  
    ```docker build -t testtesttest_kandi .```

2. To run 1 time  
    ```docker run --gpus all --shm-size 8GB -v "$(pwd):/app" -v /pathtodata/data:/data testtesttest_kandi python /app/run.py /data/1.jpg /data/2.jpg /data/output```

3. Or run container detached and run infer several times without removing container  
    ```docker run -d --name test2 --gpus all --shm-size 8GB -v "$(pwd):/app" -v /pathtodata/data:/data testtesttest_kandi sleep inf```    
    
    ```docker exec -it test2 python /app/run.py /data/1.jpg /data/2.jpg /data/output```

Example:  
 
<img src="static/1.jpg" width="300">+
<img src="static/2.jpg" width="145">=
<img src="static/test1_result.png" width="200">  


<img src="static/3.jpg" width="300">+
<img src="static/4.jpg" width="150">=
<img src="static/test2_result.png" width="200">