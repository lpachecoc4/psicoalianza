@UserStory
Feature: User story

    The user is able to create and cosult a hiring process

Scenario: The user creates and consults a hiring process
Given the user has the following data
|   key                  |   value               |
| proceso_nombre         | Proceso de prueba1224 |
| fecha_cierre           | 2023-12-31            |
| numero_vacantes        | 3                     |
| proceso_estado         | true                  |
| verificacion_identidad | true                  |
And the user adds the following prueba
|   key            | value |
| id_prueba        | 1     |
| id_perfil        | 18    |
| valor_porcentual | 100   |
When the user sends a POST request to create a proceso
Then the response status code should be '200'
And the response data should have
|   key                  |   value               |
| proceso_nombre         | Proceso de prueba1224 |
| fecha_cierre           | 2023-12-31            |
| numero_vacantes        | 3                     |
| estado                 | true                  |
| verificacion_identidad | true                  |
And the pruebas should have
|   key            | value |
| id_prueba        | 1     |
| id_perfil        | 18    |
| valor_porcentual | 100   |
