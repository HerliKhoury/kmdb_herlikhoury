# kmdb_herlikhoury

Aplicação que gerencia usuários, filmes e reviews.


### Endpoints da aplicação:
| Método | Endpoint | Objetivo | Autorização Token |
|---|---|---|---|
| `POST` | `/api/users/` | Cria um usuário | `Não` |
| `POST` | `/api/login/` |Autenticar um usuário e retornar um token de acesso | `Não` |
| `GET` | `/api/users/` |Listar todos os usuários | `Sim` |
| `GET` | `/api/movies/` |Listar todos os filmes | `Não` |
| `POST` | `/api/movies/` |Criação de um filme | `Sim` |
| `POST` | `/api/movies/<int:movie_id>/reviews/` |Criação de uma nova review para o filme | `Sim` |
| `GET` | `/api/movies/<int:movie_id>/reviews/` |Listagem das reviews do filme em questão | `Não` |

### Diagrama de Entidade de Relacionamento

[Imgur](https://i.imgur.com/qg6TTlX.jpg)