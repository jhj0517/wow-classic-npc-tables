# wow-classic-npc-tables
Since Wow does not provide an API like `GetNPCInfo()`, 
these are manual tables for classic NPC names.

### Logic
`ClassicNPCTables\ClassicNPCTables.lua` only loads tables that are needed with `LoadAddOn()`, to reduce loading time for huge tables.

### Usage
You should add `## Dependencies: ClassicNPCTables` to the .toc file header and use it like

```
id_to_npc = ClassicNPCTables:getIdToNPCTableByLocale(localeCode)
npc_to_id = ClassicNPCTables:getNPCToIdTableByLocale(localeCode)
```
