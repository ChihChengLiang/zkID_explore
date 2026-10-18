You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan. Work alone; read no repository file other than the ones named here, and do not look at other agents' output.

TASK CELL
Setting where the verifier works: peer second-hand trade (OSM: second_hand)
The verifier needs to establish: has sold at least N items with no disputes
Kind of claim (predicate type): aggregate
Today the verifier collects the information under this condition: commercial convenience: the verifier collects it because it is easy or helps its business (marketing, fraud screening, habit), with no legal duty
The fact originates in: commerce; it is used in: commerce
Who could sign the claim is open: you name the issuer (a government body, company, school, hospital, community body, platform or even a peer).

INSPIRATION MATERIAL (real excerpts from other settings). You MUST use at least two of these six items as structural inspiration:
- id: rd-singpass-myinfo-minimal-request
  situation: A service provider needs a few verified fields for one purpose, but the retrieval interface returns a broad profile and the only limit is a policy rule on the partner.
  original setting: Singpass MyInfo partners retrieve citizen data on consent, and the developer rules tell partners not to over-collect beyond what a single purpose needs.
  mechanism: Consent-gated retrieval of named MyInfo fields, with a rule to request only needed data and purge unsubmitted drafts. (outcome: partial)
  evidence: "Do not over-collect data, where this is not required for business purposes or legal reasons."
- id: rd-google-wallet-zkp-age-no-linkage
  situation: A gatekeeper needs one yes/no fact about a holder, and the proof it receives must not reveal the underlying birth date or let the issuer or the gatekeeper track the holder.
  original setting: Apps asking for age or identity through Google Wallet's digital ID receive shared data; the vendor says it uses zero-knowledge proofs so a verifier learns only the claim.
  mechanism: Zero-knowledge proof on ISO 18013-7 mdocs for an over-18 statement, device-bound transactions, no server-side storage of credential data. (outcome: works)
  evidence: "ZKP ensures that presentations are not identifiable or trackable by the issuer, the relying party, or Google."
- id: an-a-oauth-scopes
  situation: A holder asks a verifier for a credential covering more attributes than the single fact the relying party needs, and the issuer has no obligation to honour a narrower request.
  original setting: A client asks for broad access scopes to a resource server when it needs only one narrow permission, and the user approves the broader grant.
  mechanism: The client states a scope parameter in the request, and the authorization server returns the granted scope in the token response; the server may grant less than requested. (outcome: partial)
  evidence: "The authorization server MAY fully or partially ignore the scope requested by the client, based on the authorization server policy or the resource owner's instructions."
- id: tw-bank-deposit-dual-id-check
  situation: A bank must verify who a person is before opening an account, which means examining identity documents, but the cited rule does not say whether copies are kept or for how long.
  original setting: 金管會函釋：金融機構受理開立存款帳戶，應實施雙重身分證明文件查核及確認客戶身分之措施，以防制金融犯罪。
  mechanism: Dual identity-document inspection at account opening; retention and copy handling not specified in the cited text. (outcome: partial)
  evidence: "應實施雙重身分證明文件查核及確認客戶身分"
- id: tw-platform-gym-id-card-copies-interp
  situation: A service provider signing up a customer must check identity and payment, but it asks for full front-and-back copies of identity and card documents, and the regulator leaves whether that exceeds the purpose to case-by-case fact-finding.
  original setting: 健身中心於簽立會員契約時要求消費者提供身分證正反面影本及信用卡正反面影本，是否逾越特定目的必要範圍。
  mechanism: None stated; the letter says less-intrusive alternatives must be considered but names none. (outcome: unknown)
  evidence: "健身中心業者於簽立會員契約時，要求消費者提供身分證正反面影本"
- id: an-b-jury-selection
  situation: Someone must be drawn from a pool and seated for a task without the wider public learning who they are, but the default rule can flip to full publication of the identities of everyone selected, with confidentiality only as a judge-level exception.
  original setting: A federal district plan may make juror names public, but may also let a judge keep those names confidential where the interests of justice require.
  mechanism: Judge-discretionary confidentiality of juror names under a court's jury selection plan; no technical mechanism specified. (outcome: partial)
  evidence: "If the plan permits these names to be made public, it may nevertheless permit the chief judge of the district court"

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan, each with a different verifier party or situation, where today the verifier collects far more than it needs and the claim above would be enough. Do not repeat the cell text as the idea; make each moment specific. Be honest in why_zk if law or practice makes it weak.

For each idea, `inspired_by` must list the seeds you actually used. Each `borrowed_aspect` must be one sentence of the form "In <seed>, <X> does <Y>; here, <Z> plays that role", i.e. a mapping, not a vague echo. Every one of the six seeds does not have to be used, but each idea must cite at least one, and the three ideas together at least two different seeds.

Write ONLY a JSON list of 3 objects to ideas2/secondhand-seller__D.json (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (a list of {"seed_id": ..., "borrowed_aspect": ...}). Use only the Write tool for that one file. Reply with the single word DONE.
