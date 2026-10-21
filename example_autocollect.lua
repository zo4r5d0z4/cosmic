-- Example Script: Auto-Collect Nearby Items
-- Compatible with Cosmic Executor (100% sUNC)
-- Usage: Paste in Cosmic script editor and click Execute

local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local LocalPlayer = Players.LocalPlayer

local AUTO_COLLECT_ENABLED = true
local COLLECT_RANGE = 50

local function getNearbyItems()
    local items = {}
    for _, obj in ipairs(workspace:GetDescendants()) do
        if obj:IsA("BasePart") and obj:FindFirstChild("Collectable") then
            local dist = (obj.Position - LocalPlayer.Character.HumanoidRootPart.Position).Magnitude
            if dist <= COLLECT_RANGE then
                table.insert(items, obj)
            end
        end
    end
    return items
end

local function collectItem(item)
    fireproximityprompt(item:FindFirstChild("ProximityPrompt") or item:FindFirstChildWhichIsA("ProximityPrompt"))
end

local function mainLoop()
    while AUTO_COLLECT_ENABLED do
        local items = getNearbyItems()
        for _, item in ipairs(items) do
            pcall(collectItem, item)
        end
        task.wait(0.5)
    end
end

print("[Cosmic] Auto-Collect script loaded")
print("[Cosmic] Range: " .. COLLECT_RANGE .. " studs")
mainLoop()
