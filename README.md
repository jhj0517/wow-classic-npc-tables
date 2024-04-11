# wow-classic-npc-tables
Since Wow does not provide an API like `GetNPCInfo()`, 
these are manual tables for classic NPC names.

### Logic
`table_localization.lua` allows you to load the table by locale.

Call `ClassicNPCTables:getDataByLocale(localeCode, dataType)` to get a table by locale.

### Usage
Add these lines to the top level of your .toc file. 
```
## Interface: ~

PathToYourLib/NPCs/id_to_npc_classic_en.lua
PathToYourLib/NPCs/npc_to_id_classic_en.lua
PathToYourLib/NPCs/id_to_npc_classic_cn.lua
PathToYourLib/NPCs/npc_to_id_classic_cn.lua
PathToYourLib/NPCs/id_to_npc_classic_de.lua
PathToYourLib/NPCs/npc_to_id_classic_de.lua
PathToYourLib/NPCs/id_to_npc_classic_es.lua
PathToYourLib/NPCs/npc_to_id_classic_es.lua
PathToYourLib/NPCs/id_to_npc_classic_fr.lua
PathToYourLib/NPCs/npc_to_id_classic_fr.lua
PathToYourLib/NPCs/id_to_npc_classic_it.lua
PathToYourLib/NPCs/npc_to_id_classic_it.lua
PathToYourLib/NPCs/id_to_npc_classic_ko.lua
PathToYourLib/NPCs/npc_to_id_classic_ko.lua
PathToYourLib/NPCs/id_to_npc_classic_pt.lua
PathToYourLib/NPCs/npc_to_id_classic_pt.lua
PathToYourLib/NPCs/id_to_npc_classic_ru.lua
PathToYourLib/NPCs/npc_to_id_classic_ru.lua
PathToYourLib/NPCs/table_localization.lua

...
```

These all tables takes `0.000125`secs to load all those tables as I tested on my PC, which is no big deal at all.  
Of course, it would be different from PC to PC, but I think loading tables of this size is no big deal.

Get your classic NPC table like this in your main addon

```
localeCode = GetLocale()
id_to_npc = ClassicNPCTables:getDataByLocale(localeCode, "id_to_npc")
npc_to_id = ClassicNPCTables:getDataByLocale(localeCode, "npc_to_id")
```
