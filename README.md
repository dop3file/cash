# cash
Cash is an in-memory database for cache, serialized objects and "hot data"

TODO:

 2 утилиты:
 - cash-daemon
 - cash-admin

  Cash-daemon - веб сервер и core субд.
  
  Сервер должен поддерживать HTTP
  
  Должен поддерживать многопоточность
  
  Должен хранить данные в хранилище(пока хешмапе)
  
  В храналище хранятся темплейт объекты, доступ по ключу
  
  Хранилища должны быть частью инстанса базы 

  База должна сохраняться в сниппеты каждые N времени, чтоб при сбоях не потерять все данные. Подгружать их при поднятии по необходимости
  
  Cash-admin - администрация имеющихся баз данных
