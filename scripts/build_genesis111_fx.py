"""Map Genesis 111 rules text onto effect records for the site engine."""
import json
from pathlib import Path

SRC = Path(r"C:\Users\jheav\Desktop\dogetcg\DOGE-TCG-Genesis-111-Cards-and-Data\cards.json")
OUT = Path(r"C:\Users\jheav\dogestack\doginals.lol\src\lib\drops\dogetcg\g111-fx.json")

# Exact rules_text -> effects. Blank cards are absent and become [].
FX = {
    "Sun Nap. On deploy, heal 2 from an allied Doge, including this one.": [
        {"on": "deploy", "do": "healAlly", "n": 2, "who": "ally"}
    ],
    "On deploy, heal your Core by 1.": [{"on": "deploy", "do": "healCore", "n": 1}],
    "On deploy, you may give this Doge Shield.": [
        {"on": "deploy", "do": "shield", "who": "self", "opt": True}
    ],
    "On deploy, give another allied Doge Shield.": [
        {"on": "deploy", "do": "shield", "who": "other"}
    ],
    "At the start of your turn, heal 1 from this Doge.": [{"on": "start", "do": "healSelf", "n": 1}],
    "On deploy, give this Doge Shield.": [{"on": "deploy", "do": "shield", "who": "self"}],
    "On deploy, if you control another Doge, give this Doge Shield.": [
        {"on": "deploy", "do": "shield", "who": "self", "if": "other"}
    ],
    "After this Doge Secures, heal 2 from your Core.": [{"on": "secure", "do": "healCore", "n": 2}],
    "On deploy, give each other allied Doge Shield.": [
        {"on": "deploy", "do": "shield", "who": "eachOther"}
    ],
    "On deploy, heal 3 from your Core. Give this Doge Shield.": [
        {"on": "deploy", "do": "healCore", "n": 3},
        {"on": "deploy", "do": "shield", "who": "self"},
    ],
    "Look at the top 3 cards of your deck. Put them back in any order. Draw a card.": [
        {"on": "play", "do": "scry", "n": 3, "mode": "reorder"},
        {"on": "play", "do": "draw", "n": 1},
    ],
    "Heal 2 from an allied Doge. Give it Shield.": [
        {"on": "play", "do": "healAlly", "n": 2, "who": "ally", "need": "ally"},
        {"on": "play", "do": "shield", "who": "ally"},
    ],
    "Deal 3 damage to an enemy Doge. If it is defeated, heal 2 from your Core.": [
        {"on": "play", "do": "dmgEnemy", "n": 3, "need": "enemy", "dead": "healCore", "deadN": 2}
    ],
    "Return an allied Doge to your hand. Draw a card.": [
        {"on": "play", "do": "bounce", "who": "ally", "need": "ally"},
        {"on": "play", "do": "draw", "n": 1},
    ],
    "At the start of your turn, heal 1 from your Core.": [{"on": "start", "do": "healCore", "n": 1}],
    "The first time each turn an allied Doge is deployed, give it Shield.": [
        {"on": "passive", "do": "firstDeployShield"}
    ],
    "Rush.": [{"on": "kw", "do": "rush"}],
    "When defeated, heal 1 from your Core.": [{"on": "defeated", "do": "healCore", "n": 1}],
    "After this Doge hits the enemy Core, draw a card, then discard a card.": [
        {"on": "coreHit", "do": "drawDiscard", "n": 1}
    ],
    "On deploy, deal 1 damage to an enemy Doge.": [{"on": "deploy", "do": "dmgEnemy", "n": 1}],
    "The first time each turn an allied Doge moves, it gains +1 ATK for its next attack this turn.": [
        {"on": "passive", "do": "firstMoveAtk", "n": 1}
    ],
    "On deploy, deal 1 damage to an enemy Doge and 1 to its Core.": [
        {"on": "deploy", "do": "dmgEnemy", "n": 1, "alsoCore": 1}
    ],
    "On deploy, deal 2 damage to the enemy Core.": [{"on": "deploy", "do": "dmgCore", "n": 2}],
    "Lantern Hop. On deploy, you may move another allied Doge to an adjacent open allied slot.": [
        {"on": "deploy", "do": "move", "who": "other", "opt": True}
    ],
    "An allied Doge gains +2 ATK for its next attack this turn.": [
        {"on": "play", "do": "atkNext", "n": 2, "who": "ally", "need": "ally"}
    ],
    "Deal 1 damage to an enemy Doge. Draw a card.": [
        {"on": "play", "do": "dmgEnemy", "n": 1, "need": "enemy"},
        {"on": "play", "do": "draw", "n": 1},
    ],
    "Deal 2 damage to an enemy Doge. If it is defeated, deal 1 damage to its Core.": [
        {"on": "play", "do": "dmgEnemy", "n": 2, "need": "enemy", "dead": "dmgCore", "deadN": 1}
    ],
    "Deal 4 damage to an enemy Doge.": [{"on": "play", "do": "dmgEnemy", "n": 4, "need": "enemy"}],
    "The first allied Doge each turn that attacks the enemy Core gains +1 ATK for that attack.": [
        {"on": "passive", "do": "firstCoreAtk", "n": 1}
    ],
    "On deploy, you may move another allied Doge to an adjacent open allied slot.": [
        {"on": "deploy", "do": "move", "who": "other", "opt": True}
    ],
    "On deploy, look at the top 2 cards of your deck. Put them back in any order.": [
        {"on": "deploy", "do": "scry", "n": 2, "mode": "reorder"}
    ],
    "On deploy, you may move this Doge to an adjacent open allied slot.": [
        {"on": "deploy", "do": "move", "who": "self", "opt": True}
    ],
    "Phase.": [{"on": "kw", "do": "phase"}],
    "On deploy, draw a card, then discard a card.": [{"on": "deploy", "do": "drawDiscard", "n": 1}],
    "When this Doge moves, give it Shield.": [{"on": "move", "do": "shield", "who": "self"}],
    "Phase. After this Doge Secures, draw a card.": [
        {"on": "kw", "do": "phase"},
        {"on": "secure", "do": "draw", "n": 1},
    ],
    "On deploy, move an enemy Doge to an adjacent open enemy slot, if able.": [
        {"on": "deploy", "do": "move", "who": "enemy"}
    ],
    "Phase. When this Doge moves, heal 1 from it.": [
        {"on": "kw", "do": "phase"},
        {"on": "move", "do": "healSelf", "n": 1},
    ],
    "On deploy, you may move up to two other allied Doges once each to adjacent open allied slots.": [
        {"on": "deploy", "do": "move", "who": "two", "opt": True}
    ],
    "Move an allied Doge to an adjacent open allied slot.": [
        {"on": "play", "do": "move", "who": "ally", "need": "ally"}
    ],
    "Move an enemy Doge to an adjacent open enemy slot.": [
        {"on": "play", "do": "move", "who": "enemy", "need": "enemy"}
    ],
    "Return an allied Doge to your hand. An enemy Doge in its former lane takes 2 damage, if present.": [
        {"on": "play", "do": "bounce", "who": "ally", "need": "ally", "laneDmg": 2}
    ],
    "Move an allied Doge to an adjacent open allied slot. Give it Shield.": [
        {"on": "play", "do": "move", "who": "ally", "need": "ally"},
        {"on": "play", "do": "shield", "who": "moved"},
    ],
    "The first time each turn an allied Doge moves, heal 1 from it.": [
        {"on": "passive", "do": "firstMoveHeal", "n": 1}
    ],
    "At the start of your turn, look at the top card of your deck. You may put it on the bottom.": [
        {"on": "start", "do": "scry", "n": 1, "mode": "bottomOpt"}
    ],
    "When defeated, deal 1 damage to the enemy Core.": [{"on": "defeated", "do": "dmgCore", "n": 1}],
    "When defeated, you may discard a card. If you do, draw a card.": [
        {"on": "defeated", "do": "discardDraw", "n": 1, "opt": True}
    ],
    "On deploy, discard the top card of your deck if it has a card.": [{"on": "deploy", "do": "mill", "n": 1}],
    "When defeated, deal 1 damage to the enemy Doge in this lane, if present.": [
        {"on": "defeated", "do": "dmgLane", "n": 1}
    ],
    "On deploy, you may discard a card. If you do, deal 2 damage to an enemy Doge.": [
        {"on": "deploy", "do": "discardDmg", "n": 2, "opt": True}
    ],
    "On deploy, you may return a Doge of cost 1 from your discard pile to your hand.": [
        {"on": "deploy", "do": "returnDoge", "n": 1, "opt": True}
    ],
    "The first time each turn another allied Doge is defeated, deal 1 damage to the enemy Core.": [
        {"on": "passive", "do": "firstAllyDefeat", "n": 1}
    ],
    "When defeated, you may return a Doge of cost 2 or less from your discard pile to your hand.": [
        {"on": "defeated", "do": "returnDoge", "n": 2, "opt": True}
    ],
    "On deploy, you may return a Doge of cost 3 or less from your discard pile to your hand.": [
        {"on": "deploy", "do": "returnDoge", "n": 3, "opt": True}
    ],
    "On deploy, deal 3 damage to an enemy Doge if your discard pile has at least 3 cards.": [
        {"on": "deploy", "do": "dmgEnemy", "n": 3, "if": "discard3"}
    ],
    "Discard a card. If you do, draw two cards.": [{"on": "play", "do": "discardDraw", "n": 2, "need": "discard"}],
    "Return a Doge of cost 2 or less from your discard pile to your hand. Heal 1 from your Core.": [
        {"on": "play", "do": "returnDoge", "n": 2, "need": "discard"},
        {"on": "play", "do": "healCore", "n": 1},
    ],
    "Deal 4 damage to an enemy Doge. If it is defeated, put it on the bottom of its owner's deck instead of discarding it.": [
        {"on": "play", "do": "dmgEnemy", "n": 4, "need": "enemy", "dead": "bottom"}
    ],
    "Return each Doge of cost 2 or less in play to its owner's hand.": [
        {"on": "play", "do": "bounceAll", "n": 2}
    ],
    "The first time each turn you discard a card from your hand due to a card effect, heal 1 from your Core.": [
        {"on": "passive", "do": "firstDiscardHeal", "n": 1}
    ],
    "The first time each turn you return a Doge from your discard pile to your hand, deal 1 damage to the enemy Core.": [
        {"on": "passive", "do": "firstReturnCore", "n": 1}
    ],
    "On deploy, look at the top card of your deck. You may put it on the bottom.": [
        {"on": "deploy", "do": "scry", "n": 1, "mode": "bottomOpt"}
    ],
    "On deploy, look at the top 2 cards of your deck. Put them back in any order.": [
        {"on": "deploy", "do": "scry", "n": 2, "mode": "reorder"}
    ],
    "On deploy, you may reveal the top card of your deck. If it is an Item, put it into your hand.": [
        {"on": "deploy", "do": "revealItem", "opt": True}
    ],
    "On deploy, you may put a card from your hand on the bottom of your deck. If you do, draw a card.": [
        {"on": "deploy", "do": "bottomDraw", "opt": True}
    ],
    "After this Doge Secures, heal 1 from your Core.": [{"on": "secure", "do": "healCore", "n": 1}],
    "On deploy, look at the top 3 cards of your deck. Put them back in any order, then draw a card.": [
        {"on": "deploy", "do": "scry", "n": 3, "mode": "reorder"},
        {"on": "deploy", "do": "draw", "n": 1},
    ],
    "On deploy, heal 2 from your Core if you control an Item.": [
        {"on": "deploy", "do": "healCore", "n": 2, "if": "item"}
    ],
    "On deploy, give this Doge Shield if you control an Item.": [
        {"on": "deploy", "do": "shield", "who": "self", "if": "item"}
    ],
    "On deploy, look at the top 3 cards of your deck. Put one in your hand and the rest on the bottom in either order.": [
        {"on": "deploy", "do": "scry", "n": 3, "mode": "take1"}
    ],
    "On deploy, draw a card. If you control an Item, heal 2 from your Core.": [
        {"on": "deploy", "do": "draw", "n": 1},
        {"on": "deploy", "do": "healCore", "n": 2, "if": "item"},
    ],
    "Look at the top 3 cards of your deck. Put one on the bottom and the other two back in either order. Draw a card.": [
        {"on": "play", "do": "scry", "n": 3, "mode": "bottom1"},
        {"on": "play", "do": "draw", "n": 1},
    ],
    "Deal 2 damage to an enemy Doge. If you control an Item, deal 3 instead.": [
        {"on": "play", "do": "dmgEnemy", "n": 2, "alt": 3, "if": "item", "need": "enemy"}
    ],
    "Put a Tactic from your discard pile on top of your deck, if able. Draw a card.": [
        {"on": "play", "do": "tacticTop"},
        {"on": "play", "do": "draw", "n": 1},
    ],
    "You may put an Item of cost 3 or less from your hand into play. Draw a card.": [
        {"on": "play", "do": "playItem", "n": 3, "opt": True},
        {"on": "play", "do": "draw", "n": 1},
    ],
    "The first time each turn you play a Tactic, heal 1 from your Core.": [
        {"on": "passive", "do": "firstTacticHeal", "n": 1}
    ],
    "At the start of your turn, draw a card, then put a card from your hand on the bottom of your deck.": [
        {"on": "start", "do": "drawBottom"}
    ],
    "On deploy, heal 1 from another allied Doge.": [
        {"on": "deploy", "do": "healAlly", "n": 1, "who": "other"}
    ],
    "On deploy, give another allied Doge Shield if you control two other Doges.": [
        {"on": "deploy", "do": "shield", "who": "other", "if": "twoOthers"}
    ],
    "Sky Splitter. On deploy, deal 2 damage to each enemy Doge.": [
        {"on": "deploy", "do": "dmgEach", "n": 2}
    ],
    "This Doge has +1 ATK while you control two other Doges.": [
        {"on": "passive", "do": "staticAtk", "n": 1, "if": "twoOthers"}
    ],
    "On deploy, heal 1 from each other allied Doge.": [
        {"on": "deploy", "do": "healAlly", "n": 1, "who": "eachOther"}
    ],
    "After this Doge defeats an enemy Doge by attacking, heal 2 from this Doge if another allied Doge is in play.": [
        {"on": "attackKill", "do": "healSelf", "n": 2, "if": "other"}
    ],
    "On deploy, you may move another allied Doge to an adjacent open allied slot and give it Shield.": [
        {"on": "deploy", "do": "move", "who": "other", "opt": True, "thenShield": True}
    ],
    "When defeated, give each other allied Doge Shield.": [
        {"on": "defeated", "do": "shield", "who": "eachOther"}
    ],
    "On deploy, other allied Doges gain +1 ATK for their next attack this turn.": [
        {"on": "deploy", "do": "atkNext", "n": 1, "who": "eachOther"}
    ],
    "Heal 2 from an allied Doge or from your Core.": [
        {"on": "play", "do": "healAllyOrCore", "n": 2, "need": "allyOrCore"}
    ],
    "Give an allied Doge Shield. If you control three Doges, heal 1 from your Core.": [
        {"on": "play", "do": "shield", "who": "ally", "need": "ally"},
        {"on": "play", "do": "healCore", "n": 1, "if": "three"},
    ],
    "Up to two allied Doges each gain +1 ATK for their next attack this turn.": [
        {"on": "play", "do": "atkNext", "n": 1, "who": "upToTwo"}
    ],
    "Draw one card for each allied Doge, up to three cards.": [{"on": "play", "do": "drawPer", "n": 3}],
    "The first time each turn an allied Doge Secures, heal 1 from your Core.": [
        {"on": "passive", "do": "firstSecureHeal", "n": 1}
    ],
    "While you control three Doges, they each have +1 ATK.": [
        {"on": "passive", "do": "staticAtk", "n": 1, "if": "three"}
    ],
    "On deploy, you may look at the top card of your deck.": [
        {"on": "deploy", "do": "scry", "n": 1, "mode": "look", "opt": True}
    ],
    "After this Doge Secures, heal 1 from this Doge.": [{"on": "secure", "do": "healSelf", "n": 1}],
    "On deploy, heal 1 from your Core. If you control an Item, heal 2 instead.": [
        {"on": "deploy", "do": "healCore", "n": 1, "alt": 2, "if": "item"}
    ],
    "On deploy, you may discard an Item you control. If you do, draw two cards.": [
        {"on": "deploy", "do": "discardItemDraw", "n": 2, "opt": True}
    ],
    "On deploy, give this Doge Shield. You may move it to any open allied slot.": [
        {"on": "deploy", "do": "shield", "who": "self"},
        {"on": "deploy", "do": "move", "who": "any", "opt": True},
    ],
    "Heal 2 from your Core.": [{"on": "play", "do": "healCore", "n": 2}],
    "Move an allied Doge to an adjacent open allied slot.": [
        {"on": "play", "do": "move", "who": "ally", "need": "ally"}
    ],
    "Deal 1 damage to an enemy Doge. Draw a card.": [
        {"on": "play", "do": "dmgEnemy", "n": 1, "need": "enemy"},
        {"on": "play", "do": "draw", "n": 1},
    ],
    "Deal 2 damage to an enemy Doge.": [{"on": "play", "do": "dmgEnemy", "n": 2, "need": "enemy"}],
    "Draw two cards, then discard a card.": [{"on": "play", "do": "drawDiscard", "n": 2}],
    "Deal 3 damage to an enemy Doge. If it is defeated, heal 1 from your Core.": [
        {"on": "play", "do": "dmgEnemy", "n": 3, "need": "enemy", "dead": "healCore", "deadN": 1}
    ],
}


def main() -> None:
    cards = json.loads(SRC.read_text(encoding="utf-8"))
    out = {}
    missing = []
    for card in cards:
        text = card["rules_text"].strip()
        if not text:
            out[card["id"]] = []
            continue
        if text not in FX:
            missing.append(f"{card['id']} {text}")
            continue
        out[card["id"]] = FX[text]
    if missing:
        raise SystemExit("unmapped\n" + "\n".join(missing))
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"wrote {len(out)} cards")


if __name__ == "__main__":
    main()
