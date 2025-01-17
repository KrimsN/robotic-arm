# Тесты

## Общие условия ##

Производится решение задачи, описываемой файлом files/test-task.json. Установлено минимальное значение феромона, равное 1E-12 (т. е. ниже этого уровня феромон не опускается). Весовая функция возвращает длину шага сетки, если ребро существует, и +inf в противном случае.

## Наборы тестов ##

Существует набор параметров, называемый базовым. Остальные наборы параметров отличаются от базового лишь одним параметром. Параметр количества итераций остается постоянным и равен 100.

Обозначения параметров:
+ &alpha; - параметр, определяющий влияние кол-ва феромона на выбор;
+ &beta; - параметр, определяющий влияние веса ребра на выбор;
+ &gamma; - параметр, определяющий влияние направления движения относительно кратчайшего направления до конечной точки на выбор;
+ &phi; - начальный уровень феромона;
+ &rho; - скорость испарения феромона;
+ Q - количество феромона, откладываемое муравьем;
+ N - количество муравьев.

| № | &alpha; | &beta; | &gamma; | &phi; | &rho; | Q | N | Выполнен | Примечания |
|:- | ------: | -----: | ------: | ----: | ----: | -:| -:| -------- | :--------- |
|0|1.0|1.0|0.25|1E-9|0.25|1.0|64|&#9745;|Базовый набор параметров|
|1|0.0|1.0|0.25|1E-9|0.25|1.0|64|&#9745;|Граничный случай|
|2|0.5|1.0|0.25|1E-9|0.25|1.0|64|&#9744;||
|3|1.2|1.0|0.25|1E-9|0.25|1.0|64|&#9744;||
|4|1.0|0.0|0.25|1E-9|0.25|1.0|64|&#9744;|Граничный случай|
|5|1.0|0.5|0.25|1E-9|0.25|1.0|64|&#9744;||
|6|1.0|1.2|0.25|1E-9|0.25|1.0|64|&#9744;||
|7|1.0|1.0|0.0|1E-9|0.25|1.0|64|&#9744;|Граничный случай; Не завершается|
|8|1.0|1.0|0.5|1E-9|0.25|1.0|64|&#9745;||
|9|1.0|1.0|1.0|1E-9|0.25|1.0|64|&#9745;||
|10|1.0|1.0|0.25|1E-7|0.25|1.0|64|&#9744;||
|11|1.0|1.0|0.25|1E-5|0.25|1.0|64|&#9745;||
|12|1.0|1.0|0.25|1E-3|0.25|1.0|64|&#9745;||
|13|1.0|1.0|0.25|1E-9|0.0|1.0|64|&#9745;|Граничный случай|
|14|1.0|1.0|0.25|1E-9|0.5|1.0|64|&#9745;||
|15|1.0|1.0|0.25|1E-9|1.0|1.0|64|&#9745;|Граничный случай|
|16|1.0|1.0|0.25|1E-9|0.25|0.1|64|&#9744;||
|17|1.0|1.0|0.25|1E-9|0.25|10.0|64|&#9745;||
|18|1.0|1.0|0.25|1E-9|0.25|1.0|128|&#9744;|Очень долго!|
|19|1.0|1.0|0.25|1E-9|0.25|1.0|1|&#9745;||
|20|1.0|1.0|0.25|1E-9|0.25|1.0|2|&#9745;||
|21|1.0|1.0|0.25|1E-9|0.25|1.0|4|&#9745;||
|22|1.0|1.0|0.25|1E-9|0.25|1.0|8|&#9745;||
|23|1.0|1.0|0.25|1E-9|0.25|1.0|16|&#9745;||
|24|1.0|1.0|0.25|1E-9|0.25|1.0|32|&#9744;||
|25|1.0|1.0|0.25|1E-9|0.75|1.0|64|&#9745;||
|26|1.0|1.0|0.25|1E-9|0.25|1.0|256|&#9744;|Очень долго!|
|27|1.0|1.0|0.25|1E-9|0.25|1.0|512|&#9744;|Очень долго!|
