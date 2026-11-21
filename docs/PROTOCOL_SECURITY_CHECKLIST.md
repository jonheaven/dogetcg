# DOGE TCG — Protocol and Operational Security Checklist

## Trust boundaries
Dogecoin Core verifies transactions, not DOGE TCG pack issuance, edition supply, reveal fairness, or gameplay. These are metaprotocol/indexer/application rules and must be independently specified and verifiable. Distinguish immutable on-chain payload from indexer interpretation and off-chain match hosting.

## Edition identity
Use immutable `card_definition_id` distinct from `edition_inscription_id`, `art_asset_hash`, `ruleset_version`, `set_id`, `mint_serial`. Separate definition rarity from edition scarcity. Specify transfer ownership at a confirmed chain height; unconfirmed assets should not count as settled.

## Pack lifecycle
States: DRAFT -> COMMITTED -> MINTED -> SEALED -> REDEEM_PENDING -> REDEEMED or FAILED_RECOVERABLE. Reorg can reverse derived states. Pack identifier and serial must be globally unique. A commitment must bind exact distribution algorithm, edition pool, supply, reveal entropy procedure, and version. Specify when randomness becomes unknowable to issuer, how buyer/issuer bias is prevented, and what happens if the issuer withholds reveal. Do not claim cryptographic fairness from a Merkle root alone.

## Concurrency and failure
Test two redemption requests concurrently; redemption racing transfer; duplicate callbacks; stale indexer ownership; chain reorg during claim; coordinator outage; fee spike; partial inscription issuance; malicious UTXO construction; PSBT tampering; duplicate serial; unavailable delegated media; compromised mint key. Require recovery runbook and idempotency keys.

## Marketplace
Never assume DMP PSBT settlement semantics; read implementation and test vectors. Prevent stale listings, wrong collection/inscription IDs, wrong price/fee, change-output substitution, unsupported sighash flags, and signing prompts with unclear asset movement. Provide clear confirmation and explorer links.

## Match and account security
Domain-separated signatures with nonce/expiry, wallet auth without custody, signed session tokens, rate limits, reconnect token rotation, no hidden hand leakage via API or websocket, canonical RNG log, anti-cheat and collusion policy, account recovery and privacy retention policy.

## Public claims
Say 'Dogecoin-backed collectible ownership' and 'verifiable against published protocol rules' only when proven. Do not say 'all gameplay is on-chain', 'trustless', 'fully decentralized', or 'guaranteed fair' if matches/reveals rely on a coordinator. Disclose which actions actually write Dogecoin transactions.
