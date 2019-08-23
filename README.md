# Gephi python module

## Index
- [ToDo list](#todo-list)
- [Usage](#usage)
- [Documentation](#documentation)
  - [Classes](#classes)
    - Graph
    - Node
    - Edge
    - Color
    - Position
  - Method

## ToDo list
- [x] ~~All classes~~
- [x] ~~Export to .gexf file~~
- [ ] import from .gexf file

## Usage
To use this module you have to write only the import line:
``` python
from Gephi import gephi
```

## Documentation
### Classes
#### Graph
##### Instance
```python
Graph(version, creator, description, mode, default_esge_type)
```
Variables         | Type    | Options
------------------|---------|------------------------------
Version           | String  | 1.1 - 1.2
Creator           | String  | What you want
Description       | String  | What you want
Mode              | String  | static - dynamic
default_edge_type | String  | directed - undirected - mutual

##### Method
```python
add_node(node)
```
Variables   | Type  |
------------|-------|
Node        | Node  |

```python
remove_node(node)
```
Variables   | Type  |
------------|-------|
Node        | Node  |
