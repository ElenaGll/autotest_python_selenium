
Testing with Page Object Model

[task.docx](task.docx)

Необходимо автоматизировать проверку следующих сценариев:

Поиск в яндексе  
    1) Зайти на ya.ru  
    2) Проверить наличие поля поиска  
    3) Ввести в поиск ozon  
    4) Проверить, что появилась таблица с подсказками (suggest)   
    5) При нажатии Enter появляется таблица результатов поиска  
    6)  В первых 5 результатах есть ссылка на ozon  

Картинки на яндексе   
    1) Зайти на ya.ru  
    2) Ссылка «Картинки» присутствует на странице  
    3) Кликаем на ссылку  
    4) Проверить, что перешли на url https://ya.ru/images/  
    5) Открыть 1 категорию, проверить что открылась, в поиске верный текст  
    6) Открыть 1 картинку , проверить что открылась  
    7) При нажатии кнопки вперед  картинка изменяется  
    8) При нажатии кнопки назад картинка изменяется на изображение из шага 6. Необходимо проверить, что это то же изображение.  
 
Правила выполнения задания:  
    1) Автотесты реализованы на Python3 и Selenium Webdriver  
    2) Необходимо использовать тестовый framework pytest  
    3) Реализовать PageObject паттерн   
