# django-microservices


```
    Ý tưởng từ sẽ lấy dữ liệu từ db của model user từ  "mysite" lưu thành file json \n
    Sau đó từ file json đó import sang db của "microserviceapp"  
```

```
    data.json trong folder "mysite" chính là dữ liệu lấy ra từ db "mysite" \n
    data.json trong folder "microserviceapp" là file data.json trong folder "mysite"
```

## 1.Exact data từ mysite
```
     cd mysite
     chạy lệnh terminal:  python manage.py runserver 127.0.0.1:8081
     tài khoản  superadmin
     username: trimai
     password: 123456
     vào  http://127.0.0.1:8081/admin để thêm các bảng ghi (Bảng Users)
     http://127.0.0.1:8081/users (API getAllUser)
    file populate_data trong folder microserviceapp/management/commands để exact data từ db
     để exact data sang file json :
        chạy terminal   
        python manage.py fetch_data > data.json
```

## 2. Populate data vào microserviceapp
```
    cd microserviceapp
    chạy lệnh terminal:  python manage.py runserver 127.0.0.1:8080
    tài khoản  superadmin
    username: microservices
    password: 123456
    file fetch_data trong folder microserviceapp/management/commands để populate data
    để populate data từ file json :
        copy data.json từ mysite sang microserviceapp
        chạy terminal   
            cat data.json | python manage.py populate_data
    truy cập
        http://127.0.0.1:8080/users để kiểm tra data đã dc populate chưa
```
