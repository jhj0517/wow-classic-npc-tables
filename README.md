# wow-classic-npc-tables
Scraped from [Wowhead](https://www.wowhead.com/).

Since Wow does not provide an API like `GetName()` for NPCs in WowClassic, these are manual tables for NPC names.

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

Get your classic NPC table like this in your main addon

```
localeCode = GetLocale()
id_to_npc = ClassicNPCTables:getDataByLocale(localeCode, "id_to_npc")
npc_to_id = ClassicNPCTables:getDataByLocale(localeCode, "npc_to_id")
```

### Table Loading Time

These all tables takes `0.000125`secs to load as I tested on my PC, which is no big deal at all.  
Of course, it would be different from PC to PC, but I think loading tables of this size is no big deal.

