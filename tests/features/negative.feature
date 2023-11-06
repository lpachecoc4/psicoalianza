@Negative
Feature: Negative test cases
    The API should return specific errors when a bad request is sent when creating processes.


Scenario: The user is not able to create a process with a repeated name
Given the user has the following data
|   key                  |   value              |
| proceso_nombre         | Proceso de prueba123 |
| fecha_cierre           | 2023-12-31           |
| numero_vacantes        | 3                    |
| proceso_estado         | true                 |
| verificacion_identidad | true                 |
And the user adds the following prueba
|   key            | value |
| id_prueba        | 1     |
| id_perfil        | 18    |
| valor_porcentual | 100   |
When the user sends a POST request to create a proceso
Then the response status code should be '422'
And the error message should be 'El nombre del proceso ya existe.'


Scenario: The user is not able to create a process with a passed date
Given the user has the following data
|   key                  |   value              |
| proceso_nombre         | Proceso de prueba12  |
| fecha_cierre           | 2022-12-31           |
| numero_vacantes        | 3                    |
| proceso_estado         | true                 |
| verificacion_identidad | true                 |
And the user adds the following prueba
|   key            | value |
| id_prueba        | 1     |
| id_perfil        | 18    |
| valor_porcentual | 100   |
When the user sends a POST request to create a proceso
Then the response status code should be '422'
And the error should be 'El campo fecha_cierre debe ser mayor o igual a 2023-11-05'

Scenario: The user is not able to create a process with wrong percentages
Given the user has the following data
|   key                  |   value              |
| proceso_nombre         | Proceso de prueba12  |
| fecha_cierre           | 2023-12-31           |
| numero_vacantes        | 3                    |
| proceso_estado         | true                 |
| verificacion_identidad | true                 |
And the user adds the following prueba
|   key            | value |
| id_prueba        | 1     |
| id_perfil        | 18    |
| valor_porcentual | 80    |
And the user adds the following prueba
|   key            | value |
| id_prueba        | 2     |
| id_perfil        | 16    |
| valor_porcentual | 10    |
When the user sends a POST request to create a proceso
Then the response status code should be '422'
And the error should be 'La sumatoria del valor porcentual de las pruebas debe ser 100, actualmente suma: 90'
