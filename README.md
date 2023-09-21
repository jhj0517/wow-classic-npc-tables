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

## Publish
When you publish your addon with this plugin-addon, you simply pack it into a .zip file when you upload it to CurseForge.

For example:
```
YourAddon.Zip
.
├── YourAddon
├── ClassicNPCTables
├── ClassicNPCTables_en
├── ClassicNPCTables_cn
├── ClassicNPCTables_pt
├── ClassicNPCTables_de
├── ClassicNPCTables_es
├── ClassicNPCTables_fr
├── ClassicNPCTables_it
├── ClassicNPCTables_ko
└── ClassicNPCTables_ru
```

Although there are many AddOns, since they are set to `## LoadOnDemand= 1`, users will only selectively load the Addon they need based on the locale.
