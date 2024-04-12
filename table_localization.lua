ClassicNPCTables = ClassicNPCTables or {}

local localeMap = {
    ["koKR"] = {
        id_to_npc = id_to_npc_ko,
        npc_to_id = npc_to_id_ko
    },
    ["frFR"] = {
        id_to_npc = id_to_npc_fr,
        npc_to_id = npc_to_id_fr
    },
    ["deDE"] = {
        id_to_npc = id_to_npc_de,
        npc_to_id = npc_to_id_de
    },
    ["enGB"] = {
        id_to_npc = id_to_npc_en,
        npc_to_id = npc_to_id_en
    },
    ["enUS"] = {
        id_to_npc = id_to_npc_en,
        npc_to_id = npc_to_id_en
    },
    ["itIT"] = {
        id_to_npc = id_to_npc_it,
        npc_to_id = npc_to_id_it
    },
    ["zhCN"] = {
        id_to_npc = id_to_npc_cn,
        npc_to_id = npc_to_id_cn
    },
    ["zhTW"] = {
        id_to_npc = id_to_npc_cn,
        npc_to_id = npc_to_id_cn
    },
    ["ruRU"] = {
        id_to_npc = id_to_npc_ru,
        npc_to_id = npc_to_id_ru
    },
    ["esES"] = {
        id_to_npc = id_to_npc_es,
        npc_to_id = npc_to_id_es
    },
    ["esMX"] = {
        id_to_npc = id_to_npc_es,
        npc_to_id = npc_to_id_es
    },
    ["ptBR"] = {
        id_to_npc = id_to_npc_pt,
        npc_to_id = npc_to_id_pt
    },
    -- Default table to English
    ["default"] = {
        id_to_npc = id_to_npc_en,
        npc_to_id = npc_to_id_en
    }
}

function ClassicNPCTables:getDataByLocale(localeCode, dataType)
    -- If the given localeCode doesn't exist in the map, use "default"
    local localeData = localeMap[localeCode] or localeMap["default"]
    return localeData[dataType]
end


-- Use it like this in your main addon
-- localeCode = GetLocale()
-- id_to_npc_table = ClassicNPCTables:getDataByLocale(localeCode, "id_to_npc")
-- npc_to_id_table = ClassicNPCTables:getDataByLocale(localeCode, "npc_to_id")
