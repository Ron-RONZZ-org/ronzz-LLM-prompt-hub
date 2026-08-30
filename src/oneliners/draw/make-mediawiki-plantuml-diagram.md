## TASK: make plantuml diagram(s)

## Topic:

## Requirements

- when possible, use "bluegray" theme
- this uml will be rendered by the "Diagrams" MediaWiki extension on a live MediaWiki instance
  - therefore, respond with a code block with plantuml code wrapped between <uml></uml> 
  - be self-contained or use [stlib](https://plantuml.com/stdlib): PlantUML runs in its SANDBOX security profile: !include of local files and URLs is disabled.
- {{include:format/plantuml}}
- example

```
<uml>
@startuml
!theme bluegray
node "Server" {
  [Web] --> [App]
}
node "Database" {
  database "Postgres" as pg
}
[App] --> pg
@enduml
</uml>
```
