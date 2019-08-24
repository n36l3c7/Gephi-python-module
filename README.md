# Gephi python module

## Index
- [ToDo list](#todo-list)
- [Usage](#usage)
- [Documentation](#documentation)
  - [Classes](#classes)
    - [Graph](#graph)
    - [Node](#node)
    - [Edge](#edge)
    - [Color](#color)
    - [Position](#position)
  - [Methods](#methods)

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
Variables         | Type    | Nullable  | Options
------------------|---------|:---------:|------------------------------
Version           | String  |     ✘     | 1.1 - 1.2
Creator           | String  |     ✔     | What you want
Description       | String  |     ✔     | What you want
Mode              | String  |     ✘     | static - dynamic
default_edge_type | String  |     ✘     | directed - undirected - mutual
___


##### Method
```python
add_node(node)
```
Return: 
  - **0**: Node has not been added
    - *Node already exist*
  - **1**: Node has been added

Variables   | Nullable  | Type           |
------------|:---------:|----------------|
Node        |     ✘     | [Node](#node)  |
___

```python
remove_node(node)
```
Return: 
  - **0**: Node has not been removed
    - *Node doesn't exist*
  - **1**: Node has been removed
  
Variables   | Nullable  | Type           |
------------|:---------:|----------------|
Node        |     ✘     | [Node](#node)  |
___

```python
node_exist(node)
```
Return: 
  - **false**: Node already doesn't exist in graph node list
  - **true**: Node already exist in graph node list
  
Variables   | Nullable  | Type           |
------------|:---------:|----------------|
Node        |     ✘     | [Node](#node)  |
___

```python
node_id_exist(node)
```
Return: 
  - **false**: Node id already doesn't exist in graph node list
  - **true**: Node id already exist in graph node list
  
Variables   | Nullable  | Type                     |
------------|:---------:|--------------------------|
Node        |     ✘     | [Node](#node) - string   |
___

```python
add_edge(edge)
```
Return: 
  - **0**: Edge has not been added
    - *Edge already exist*
    - *Edge source/target association already exist*
    - *Doesn't exist an association between edge source and a node id*
    - *Doesn't exist an association between edge target and a node id*
  - **1**: Edge has been added

Variables   | Nullable  | Type           |
------------|:---------:|----------------|
Edge        |     ✘     | [Edge](#edge)  |
___

```python
remove_edge(edge)
```
Return: 
  - **0**: Edge has not been removed
    - *Edge doesn't exist*
  - **1**: Edge has been removed
  
Variables   | Nullable  | Type           |
------------|:---------:|----------------|
Edge        |     ✘     | [Edge](#edge)  |
___

```python
Edge_exist(edge)
```
Return: 
  - **false**: Edge already doesn't exist in graph node list
  - **true**: Edge already exist in graph node list
  
Variables   | Nullable  | Type           |
------------|:---------:|----------------|
Edge        |     ✘     | [Edge](#edge)  |
___

```python
edge_association_exist(edge)
```
Return: 
  - **false**: Edge id already doesn't exist in graph node list
  - **true**: Edge id already exist in graph node list
  
Variables   | Nullable  | Type           |
------------|:---------:|----------------|
Edge        |     ✘     | [Edge](#edge)  |
___

#### Node
#### Instance
```python
Node(id, label, color, position, size, shape)
```
Variables         | Type    | Nullable  | Options
------------------|---------|:---------:|------------------
Id                | String  |     ✘     | What you want
Label             | String  |     ✘     | What you want
Color             | Color   |     ✔     | What you want
Position          | Position|     ✔     | What you want
Size              | Numeric |     ✔     | What you want
Shape             | Numeric |     ✔     | What you want
___

#### Method
```python
to_string()
```
___

### Edge
#### Instance
```python
Edge(id, label, type, source, target, weight)
```
Variables         | Type    | Nullable  | Options
------------------|---------|:---------:|------------------
Id                | String  |     ✘     | What you want
Label             | String  |     ✔     | What you want
Type              | String  |     ✘     | directed - undirected - mutual
Source            | String  |     ✘     | An existing node id
Target            | String  |     ✘     | An existing node id
Weight            | Numeric |     ✔     | What you want
___

#### Method
```python
to_string()
```
___

### Color
#### Instance
```python
Color(r, g, b)
```
Variables         | Type    | Nullable  | Options
------------------|---------|:---------:|------------------
R                 | Numeric |     ✘     | Value from 0 to 255
G                 | Numeric |     ✘     | Value from 0 to 255
B                 | Numeric |     ✘     | Value from 0 to 255
___

### Position
#### Instance
```python
Position(x, y, z)
```
Variables         | Type    | Nullable  | Options
------------------|---------|:---------:|------------------
X                 | Numeric |     ✘     | What you want
Y                 | Numeric |     ✘     | What you want
Z                 | Numeric |     ✘     | What you want
___
## Methods

```python
create_gefx_file(graph, filename)
```
Variables         | Type            | Nullable  | Options
------------------|-----------------|:---------:|------------------
Graph             | [Graph](#graph) |     ✘     | What you want
filename          | String          |     ✘     | File name . extension
