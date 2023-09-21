ClassicNPCTables = ClassicNPCTables or {}
ClassicNPCTables.data = ClassicNPCTables.data or {}

local localeToAddOns = {
    ["koKR"] = "ClassicNPCTables_ko",
    ["frFR"] = "ClassicNPCTables_fr",
    ["deDE"] = "ClassicNPCTables_de",
    ["enGB"] = "ClassicNPCTables_en",
    ["enUS"] = "ClassicNPCTables_en",
    ["itIT"] = "ClassicNPCTables_it",
    ["zhCN"] = "ClassicNPCTables_cn",
    ["zhTW"] = "ClassicNPCTables_cn",
    ["ruRU"] = "ClassicNPCTables_ru",
    ["esES"] = "ClassicNPCTables_es",
    ["esMX"] = "ClassicNPCTables_es",
    ["ptBR"] = "ClassicNPCTables_pt",
    ["default"] =  "ClassicNPCTables_en" -- Default to English table path
}

function ClassicNPCTables:loadDataForLocale(localeCode)
    local addonName = localeToAddOns[localeCode]
    if not IsAddOnLoaded(addonName) then
        local loaded, reason = LoadAddOn(addonName)
        if not loaded then
            print("ClassicNPCTables: Failed to load data for locale: ", localeCode, " Reason: ", reason)
            return false
        end
    end
    return true
end

function ClassicNPCTables:getIdToNPCTableByLocale(localeCode)
    if not ClassicNPCTables.data[localeCode] then
        if not self:loadDataForLocale(localeCode) then return {} end

        local shortLocale = string.sub(localeCode, 1, 2)
        if localeCode == "zhCN" or localeCode == "zhTW" then
            shortLocale = "cn"
        end
        ClassicNPCTables.data[localeCode].id_to_npc = _G["id_to_npc_" .. shortLocale]
    end
    return ClassicNPCTables.data[localeCode].id_to_npc or {}
end

function ClassicNPCTables:getNPCToIdTableByLocale(localeCode)
    if not ClassicNPCTables.data[localeCode] then
        if not self:loadDataForLocale(localeCode) then return {} end

        local shortLocale = string.sub(localeCode, 1, 2)
        if localeCode == "zhCN" or localeCode == "zhTW" then
            shortLocale = "cn"
        end
        ClassicNPCTables.data[localeCode].npc_to_id = _G["npc_to_id_" .. shortLocale]
    end
    return ClassicNPCTables.data[localeCode].npc_to_id or {}
end

-- use in main addon like
-- id_to_npc = ClassicNPCTables:getIdToNPCTableByLocale(localeCode)
-- npc_to_id = ClassicNPCTables:getNPCToIdTableByLocale(localeCode)