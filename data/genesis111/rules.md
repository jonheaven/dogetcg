# Genesis 111

DOGE TCG · Tabletop rules · Playtest v0.1

Lead a pack of Shibes across three routes of the Dogecoin network. Break through to the opposing Core or secure enough open lanes to broadcast the winning Signal.

## 1. Get ready

- For two players. Each needs a 30-card deck, a Core tracker, a Signal tracker, a Charge tracker, and damage and Shield markers. Coins or dice work as markers.
- Lay out three shared lanes from left to right. Each lane has one Doge slot per player. Opposing slots face each other. Keep up to two Items beside your Core, outside the lanes.
- Your Core starts at 20, Signal at 0 and maximum Charge at 0. Shuffle independently. Flip a coin for the first player.
- Draw five cards. In starting-player order, each player may set aside any number of those cards face down once, draw the same number, then shuffle the set-aside cards into their deck.
- Keep hands and decks hidden. Cores, Signal, Charge, Items, lanes, and discard piles are public. A deck's remaining count is public.

## 2. Build a 30-card deck

Pick one faction and use cards from that faction plus up to six Neutral cards. Include at most two copies of a card ID, or one for a Legendary. A deck's faction is public. Common, Uncommon and Rare share the same copy limit. Foils and regular finishes share card identity, rules and deck limits.

| Faction | Plan | Watch for |
| Ironclad | Shield and healing buy time to hold open lanes. | A shield breaks on the next hit, even a small one. |
| Outriders | Rush and damage Tactics open lanes fast. | Spend removal carefully against durable Doges. |
| Ghostline | Move your Doges and reroute defenders. | Keep a slot free so you have somewhere to move. |
| Ashbound | Recycle cheap Doges and turn defeats into Core damage. | Build your discard pile before committing to a payoff. |
| Runekeepers | Control future draws and combine Items with Tactics. | Protect your Core while you assemble your board. |
| Wildpack | Fill all three lanes for pack bonuses. | Plan how to rebuild after a multi-target attack. |

## 3. Your turn

1. Start. Ready all your exhausted Doges. Increase your maximum Charge by 1 to a cap of 8. Refill available Charge to that maximum. Resolve your start-of-turn effects in your chosen order. Then draw one card. The starting player skips this regular draw on the match's first turn.
2. Act. In any order, play cards and take actions with ready Doges. Resolve each play or action fully before the next. Actions come from the player whose turn it is. Triggered effects may resolve on either turn. On the match's first turn, attacks are unavailable.
3. End. If you have more than ten cards in hand, put chosen excess cards into your discard pile. End-of-turn hand cleanup is a rules action. Clear remaining temporary attack bonuses and unused Charge. Pass to your opponent.

## 4. Play a card

- Doge. Pay its Charge cost, put it into an open slot on your side, and exhaust it. On-deploy abilities happen now. Damage markers, Shield and attack bonuses start fresh each time a Doge enters play.
- Tactic. Pay its cost, announce choices and initial targets, resolve its rules, then put it into its owner's discard pile. A Tactic becomes eligible to recover from discard after it has finished resolving.
- Item. Pay its cost and put it beside your Core. It stays in play and affects your side of the board as written. Each player has two Item slots and one in-play copy of each Item. You may discard your own Item to make room as part of placing a new one. This also applies when an effect places an Item into play.
- A card placed into play by an effect skips payment. A card's legal slot is required. An effect that forces a discard from hand needs a card in that hand. You can play a card with only optional or conditional effects even when those effects will do nothing.

## 5. Act with a Doge

- Attack. Exhaust a ready Doge. If the opposing slot holds a Doge, attack it. Both deal their current ATK to each other simultaneously, even if the defender is exhausted. Otherwise deal your Doge's ATK to the opposing Core. Clash damage persists on Doges between turns. A Doge outside the attacking lane takes damage only through card text.
- Secure. Exhaust a ready Doge in a lane whose opposing slot is empty. Gain 1 Signal. Each player can Secure a given lane once per turn and can Secure at most twice per turn. Record when a lane has been secured this turn even if the Doges in it move.
- Move. Exhaust a ready Doge to shift it one lane left or right into an open allied slot. Moves from abilities keep the Doge's current ready or exhausted state. All damage, Shield and bonuses travel with it.

## 6. Winning

You win by reaching 8 Signal, reducing the enemy Core to 0, or when your opponent fails a required draw. Check after each completed action, play or start step and all resulting triggers. If both players meet a win condition at that check, draw. After 60 total turns, if neither player wins, draw. Looking at, revealing or discarding the top of an empty deck is allowed and yields nothing.

## 7. Timing and common effects

- Shield absorbs 1 from the next positive damage event to that Doge, then expires. A Doge holds at most one Shield. Effects giving Shield to an already shielded Doge leave its Shield in place.
- Rush allows a Doge to declare an attack against a Doge on the turn it was deployed while exhausted from deployment. Once per deployment, and only if it has taken no Doge action since entering. Rush uses up its action. The match's first-turn attack restriction still applies.
- Phase allows a ready Doge, once on each of its controller's turns, to move one lane into an open allied slot without exhausting. This is a separate action while that Doge is ready.
- Heal removes existing damage up to the amount shown. A Core cannot be healed past 20. A Doge is defeated when accumulated damage reaches its HP. When a Doge leaves play, clear its markers. For discard and recovery, the card's printed Cost is used.
- ATK modifiers add together. A bonus for the next attack is consumed at declaration and applies to that combat's outgoing damage. It does not affect counter-damage when defending. Static ATK modifiers apply in either role. A Doge that returns to hand always becomes a new in-play instance if redeployed.
- For card text with a named move followed by a period, read the move name as an ability label. Shield, Rush and Phase on their own carry the glossary meaning. Printed blank rules windows have no ability.

## 8. Resolve the details

- The active player chooses a legal target for each required instruction of cards they play. The controller chooses targets for their abilities when they resolve. A Tactic needs a legal initial target for any unconditional targeting instruction. Resolve remaining clauses in order and as far as possible. An eligible required target currently absent at a trigger's resolution makes that instruction do nothing. If a clause says “if you do,” the preceding action must succeed.
- When cards ask for the top N cards, use as many as are available. You choose the order of any cards put back, unless instructed otherwise. Putting a card into hand by an effect is distinct from drawing. Place several cards on the bottom as a group in chosen order unless specified.
- For one effect or combat, take a snapshot of simultaneous damage, apply Shields and mark damage, then remove all defeated Doges together. Use their last in-play lane and controller for defeat triggers. Cards return to their owner's hand, deck, or discard as specified. The targeted Doge defeated by Burn Address still counts as defeated and fires defeat triggers. Resolve printed instructions in order and collect triggers before processing them.
- Resolve each queued trigger fully, adding newly triggered effects to the end of the queue. Groups that trigger together go active player's first, then opponent's, with each player ordering their own. A queued trigger still resolves if its source leaves play. Effects referring to a specific Doge in play lose track of it when it leaves play. Defeat triggers can use the departed Doge's last lane. Other allied Doges already defeated in the same batch do not trigger abilities requiring an in-play source to see those defeats. “First time each turn” counters belong to each in-play card instance and reset at the start of either player's turn.
- “For its next attack” bonuses apply when an attack is declared. Relay Beacon's first-Core-attack bonus is applied as part of that attack before its damage. An effect mentioning a defeated defender during an attack uses the result of the initial clash. A defeated attacker cannot heal itself.
- Track failed required draws during resolution, including multi-draw effects, then check victory once the action or step and its triggers are finished. Empty slots and empty decks remain directly inspectable as public counts.

## 9. Start with Kabosu versus Kitsunebi

Print the two starter decks at actual size. Cut the cards and put them in opaque sleeves with any spare cards behind them. Pick Ironclad to protect your Doges and Secure, or Outriders to clear the lanes and attack the Core. The remaining faction decklists are included as alternatives.

Example. Kabosu is ready in the center with a Shield and faces a 3 ATK / 3 HP Kitsunebi. Kabosu has 2 ATK / 5 HP. Kabosu attacks and exhausts. Kitsunebi takes 2 damage. Kabosu takes 2 after Shield soaks 1. Both live. With a ready Doge facing an empty slot, you could instead use a different lane to Secure for 1 Signal. An enemy in the center blocks both a center Core attack and a center Secure.
