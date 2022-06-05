1.  Установлен Nginx
    Установлен Gunicorn   
2.  Nginx настроен на отдачу статических файлов по пути http://server_name:80/public/ (Файлы Default и nginx.conf)
3.  Создан и запущен с помощью gunicorn файл простейшего WSGI-приложения(Расположено в папке gunicorn)
4.  Nginx настроен на проксирование запросов на сервер gunicorn (Файлы Default и nginx.conf)
5.  Проведено тестирование производительности с помощью ab
    $ ab -n 10 -c 2 -t 1 -v 2 http://192.168.56.102/public/index.html
    Concurrency Level:      2
    Time taken for tests:   1.004 seconds
    Complete requests:      1340
    Failed requests:        0
    Total transferred:      580220 bytes
    HTML transferred:       257280 bytes
    Requests per second:    1334.74 [#/sec] (mean)
    Time per request:       1.498 [ms] (mean)
    Time per request:       0.749 [ms] (mean, across all concurrent requests)
    Transfer rate:          564.40 [Kbytes/sec] received

    Connection Times (ms)
                min  mean[+/-sd] median   max
    Connect:        0    0   0.7      0      20
    Processing:     0    1   2.6      0      38
    Waiting:        0    1   1.8      0      38
    Total:          0    1   2.7      0      38

    Percentage of the requests served within a certain time (ms)
    50%      0
    66%      1
    75%      1
    80%      2
    90%      4
    95%      6
    98%      9
    99%     12
    100%     38 (longest request)

    $ ab -n 10 -c 2 -t 1 -v 2 http://192.168.56.102/backend
    Concurrency Level:      2
    Time taken for tests:   1.001 seconds
    Complete requests:      1694
    Failed requests:        0
    Non-2xx responses:      1694
    Total transferred:      655578 bytes
    HTML transferred:       301532 bytes
    Requests per second:    1692.53 [#/sec] (mean)
    Time per request:       1.182 [ms] (mean)
    Time per request:       0.591 [ms] (mean, across all concurrent requests)
    Transfer rate:          639.66 [Kbytes/sec] received

    Connection Times (ms)
                min  mean[+/-sd] median   max
    Connect:        0    0   2.4      0      68
    Processing:     0    1   2.2      0      38
    Waiting:        0    0   1.3      0      38
    Total:          0    1   3.3      0      71

    Percentage of the requests served within a certain time (ms)
    50%      0
    66%      1
    75%      1
    80%      1
    90%      3
    95%      5
    98%      7
    99%     10
    100%     71 (longest request)

    $ ab -n 10 -c 2 -t 1 -v 2 http://127.0.0.1:8000/
    Concurrency Level:      2
    Time taken for tests:   1.001 seconds
    Complete requests:      346
    Failed requests:        0
    Total transferred:      55499 bytes
    HTML transferred:       7266 bytes
    Requests per second:    345.81 [#/sec] (mean)
    Time per request:       5.784 [ms] (mean)
    Time per request:       2.892 [ms] (mean, across all concurrent requests)
    Transfer rate:          54.17 [Kbytes/sec] received

    Connection Times (ms)
                min  mean[+/-sd] median   max
    Connect:        0    0   0.2      0       1
    Processing:     0    6   4.9      4      37
    Waiting:        0    2   3.2      1      29
    Total:          0    6   4.9      4      37

    Percentage of the requests served within a certain time (ms)
    50%      4
    66%      6
    75%      8
    80%      8
    90%     12
    95%     14
    98%     21
    99%     24
    100%     37 (longest request)