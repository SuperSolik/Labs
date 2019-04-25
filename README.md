# Labs
## lab1
Содержит файл сборки проекта CMakeLists.txt, и папку src, содержащую исходные файлы проекта (cpp файлы тестов, основных программ, файл с функциями, которые используются в программах).\
Для сборки проекта:\
```
cmake CmakeLists.txt
make
```
В результате вышеприведенных команд соберется 4 исполняемых файла - runStep1, runStep1Tests, runStep2, runStep2Tests.\
runStep1, runStep2 - для запуска программ из шагов 1 (КМП) и 2 (нахождение циклического сдвига).\
В обоих случая программа требует на вход две строки (паттерн и текст), в 1-й программе находит все вхождения паттерна в текст и выводит их в консоль, во 2-й программе определяет, является ли паттерн циклическим сдвигом текста.\
runStep1Tests, runStep2Tests - для запуска тестов к ним.
