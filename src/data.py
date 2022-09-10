try:
    uiFile = "res/MainWindow.ui"
except FileNotFoundError:
    print("[COLE:ERROR]: File ``MainWindow.ui`` not found!")

actorRoot = None

actorCatDebugToNormal = {
    "ACTORCAT_SWITCH": "Switch",
    "ACTORCAT_BG": "BG Actor",
    "ACTORCAT_PLAYER": "Player",
    "ACTORCAT_EXPLOSIVE": "Explosive",
    "ACTORCAT_NPC": "NPC",
    "ACTORCAT_ENEMY": "Enemy",
    "ACTORCAT_PROP": "Props",
    "ACTORCAT_ITEMACTION": "Item/Action",
    "ACTORCAT_MISC": "Misc",
    "ACTORCAT_BOSS": "Boss",
    "ACTORCAT_DOOR": "Door",
    "ACTORCAT_CHEST": "Chest"
}
