1.  Установлен Nginx
    Установлен Gunicorn   
2.  Nginx настроен на отдачу статических файлов по пути http://server_name:80/public/ (Файлы Default и nginx.conf)
3.  Создан и запущен с помощью gunicorn файл простейшего WSGI-приложения(Расположено в папке gunicorn)
4.  Nginx настроен на проксирование запросов на сервер gunicorn (Файлы Default и nginx.conf)
5.  Проведено тестирование производительности с помощью ab
    $ ab -n 10 -c 2 -t 1 -v 2 http://192.168.1.37/public/index.html
    Finished 16617 requests

    Server Software:        nginx/1.18.0
    Server Hostname:        192.168.1.37
    Server Port:            80

    Document Path:          /public/index.html
    Document Length:        192 bytes

    Concurrency Level:      2
    Time taken for tests:   1.004 seconds
    Complete requests:      16617
    Failed requests:        0
    Total transferred:      7195594 bytes
    HTML transferred:       3190656 bytes
    Requests per second:    16551.08 [#/sec] (mean)
    Time per request:       0.121 [ms] (mean)
    Time per request:       0.060 [ms] (mean, across all concurrent requests)
    Transfer rate:          6999.07 [Kbytes/sec] received

    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0    0   0.5      0      20
    Processing:     0    0   0.5      0      20
    Waiting:        0    0   0.0      0       1
    Total:          0    0   0.6      0      20

    Percentage of the requests served within a certain time (ms)
      50%      0
      66%      0
      75%      0
      80%      0
      90%      0
      95%      0
      98%      0
      99%      0
     100%     20 (longest request)


    $ ab -n 10 -c 2 -t 1 -v 2 http://192.168.1.37/backend
    Finished 16778 requests

    Server Software:        nginx/1.18.0
    Server Hostname:        192.168.1.37
    Server Port:            80

    Document Path:          /backend
    Document Length:        178 bytes

    Concurrency Level:      2
    Time taken for tests:   1.009 seconds
    Complete requests:      16778
    Failed requests:        0
    Non-2xx responses:      16779
    Total transferred:      6459915 bytes
    HTML transferred:       2986662 bytes
    Requests per second:    16626.96 [#/sec] (mean)
    Time per request:       0.120 [ms] (mean)
    Time per request:       0.060 [ms] (mean, across all concurrent requests)
    Transfer rate:          6251.72 [Kbytes/sec] received

    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0    0   0.4      0      19
    Processing:     0    0   0.4      0      19
    Waiting:        0    0   0.0      0       1
    Total:          0    0   0.6      0      19

    Percentage of the requests served within a certain time (ms)
      50%      0
      66%      0
      75%      0
      80%      0
      90%      0
      95%      0
      98%      0
      99%      0
     100%     19 (longest request)


    $ ab -n 10 -c 2 -t 1 -v 2 http://127.0.0.1:8000/
    Finished 11497 requests

    Server Software:        gunicorn
    Server Hostname:        127.0.0.1
    Server Port:            8000

    Document Path:          /
    Document Length:        21 bytes

    Concurrency Level:      2
    Time taken for tests:   1.000 seconds
    Complete requests:      11497
    Failed requests:        0
    Total transferred:      1839520 bytes
    HTML transferred:       241437 bytes
    Requests per second:    11496.57 [#/sec] (mean)
    Time per request:       0.174 [ms] (mean)
    Time per request:       0.087 [ms] (mean, across all concurrent requests)
    Transfer rate:          1796.34 [Kbytes/sec] received

    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0    0   0.0      0       0
    Processing:     0    0   0.1      0       2
    Waiting:        0    0   0.1      0       2
    Total:          0    0   0.1      0       2

    Percentage of the requests served within a certain time (ms)
      50%      0
      66%      0
      75%      0
      80%      0
      90%      0
      95%      0
      98%      0
      99%      0
     100%      2 (longest request)
