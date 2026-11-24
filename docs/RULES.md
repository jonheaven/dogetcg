# ÐogeTCG alpha rules — `dogetcg-alpha-1`

Normative for the match on `doginals.lol/drops/dogetcg`. The client is `doginals.lol/src/lib/drops/dogetcg/alpha.ts`. A replay is the seed plus the action list. Same seed, same decks.

This is a short, silly Shiba game. You can win by cracking Core or by holding a lane long enough to reach Signal. Turns stay small. The jokes live in the card names and the pictures.

Leave other Dogecoin card games alone. Do not import their life total, lane count, class names, keyword list, or combat gate. A printed ÐogeTCG card uses these rules.

## Match

- Two seats. You against the Kennel, or you against another holder on the command.dog table (`/dogetcg/api/match`, same process as ÐBox).
- After the set is inscribed, a seat brings the cards in that wallet. Until then both seats use the 18-card practice deck.
- Lanes are public. The other seat's hand stays hidden.
- Each player starts at 20 Core and 0 Signal.
- Win by reducing the other Core to 0, or by reaching 8 Signal, at the end of the action.
- If both would win on the same check, the match is a draw.
- After 60 plies the match is a draw.
- A player who must draw from an empty deck loses.
- A print does not add attack. The card you own is the card you play. Trading is how you get a card you did not pull.

## Resources

- Charge maximum starts at 1 on the first turn and rises by 1 each of your turns, up to 6. It refills at the start of your turn.
- You draw 1 at the start of your turn. The first player does not draw on ply 1 (both players already hold 4).
- Secure gives 1 Signal, at most twice on your turn, and only in a lane where you have a unit and the other player does not.

## Board

- Three lanes. One unit per player per lane.
- Playing a unit spends charge equal to its cost and puts it in an empty lane you choose.
- A unit cannot attack or secure on the turn it is played, unless it has quickdraw.
- Quickdraw may attack a unit in that lane on the turn it is played. It cannot hit Core and it cannot secure that turn.
- Ply 1 cannot attack at all.
- An attack against a unit deals both attacks at once. A unit at 0 health leaves. An attack into an empty opposing slot hits Core for the attacker’s attack.
- A unit that acted is exhausted until your next turn.

## Deck

Eighteen cards, one copy each, listed in the client. This is the alpha deck, not a 30-card constructed deck.

## Deferred

Rear rank, automatic promotion, relics, reactions, Guard beyond “the unit in the lane is the one in the way,” Phase, Salvage, Scry, Pack, Pierce, and the rest of the 111.
