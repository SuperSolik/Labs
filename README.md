# Labs
## lab1
Содержит файл сборки проекта CMakeLists.txt, и папку src, содержащую исходные файлы проекта (cpp файлы тестов, основных программ, файл с функциями, которые используются в программах).\
Для сборки проекта:  
```
cmake CmakeLists.txt
make
```
В результате вышеприведенных команд соберется 4 исполняемых файла - runStep1, runStep1Tests, runStep2, runStep2Tests.\
runStep1, runStep2 - для запуска программ из шагов 1 (КМП) и 2 (нахождение циклического сдвига).\
В обоих случая программа требует на вход две строки (паттерн и текст), в 1-й программе находит все вхождения паттерна в текст и выводит их в консоль, во 2-й программе определяет, является ли паттерн циклическим сдвигом текста.\
runStep1Tests, runStep2Tests - для запуска тестов к ним.
## lab2
Содержит 4 файла на языке Python: step1.py, step2.py, step1tests.py, step2tests.py.\
step1.py и step2.py - файлы, содержащие программы из 1-го и 2-го степов соответственно. Первая программа принимает на вход исходный текст, количество паттернов, и паттерны, каждый на новой строке. Программа осуществляет поиск вхождений всех паттернов в текст и выводит их в консоль. Вторая программа принимает на вход исходный текст, паттерн с символом-джокером, и символ-джокер. Программа осуществляет поиск вхождений паттерна с джокером в текст и выводит их в консоль.\
Для запуска тестов к степу 1 запустить step1tests.py, к степу 2 - step2test.py. В данных файлах реализовано подобие параметризованных тестов - программма запускает один тест, состоящий из подтестов с различными параметрами.
