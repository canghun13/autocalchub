# AutoCalcHub 인수인계 문서 (2026-09-07 기준)

> 이 문서는 새 대화 세션에서 이어받아 작업을 진행할 수 있도록 프로젝트 전체 맥락을 담은 통합 인수인계 문서입니다. Git 루트에 위치하며, 작업할 때마다 이 문서를 최신 상태로 갱신할 것.

---

## 1. 사이트 기본 정보
- 도메인: autocalchub.com / GitHub Pages 호스팅 / Cloudflare 관리, 연 $10.46
- 저장소: `github.com/canghun13/autocalchub` (public)
- GA4: G-ZH1JYG24PK
- 애드센스: ca-pub-5592663499707350
- 디자인: 다크 네이비 + 오렌지, 폰트는 Space Grotesk(제목) + Inter(본문)
- 월 운영비: 약 38,000원 (Claude Pro + 도메인 5개)

## 2. 콘텐츠 현황 (2026-09-07 기준)
- 블로그 73개, 툴 32개 (index.html 제외). 9/7 세션에서 블로그 1 + 툴 1 추가, MPG 페이지 대폭 보강.
- sitemap.xml 총 URL 118개
- **블로그 태그 카테고리 9종**: `💰 Buying a Car`, `🏦 Financing`, `⛽ Running Costs`, `⚡ Electric Vehicles`, `📈 Ownership & Value`, `🤝 Selling &amp; Trade-In`, `🚕 Gig &amp; Rideshare`, `🚨 Accidents &amp; Claims`, `🚚 Moving &amp; Relocation`. 이모지까지 정확히 맞출 것.
- **⚠️ Related Guides 헤딩이 3가지 변형**으로 존재: `<h3>Related Guides</h3>`, `<h3>Related Guides &amp; Tools</h3>`, **`<h2>Related Guides</h2>`(7개 파일)**. 일괄 스크립트 편집 시 정규식을 `<h[23][^>]*>Related Guides(?: &amp;| &)? ?(?:Tools)?</h[23]>` 로 쓸 것. h2 변형은 `<ul>` 들여쓰기가 4칸(다른 변형은 6칸)이라 삽입 문자열도 맞춰야 함.
- **블로그 전체**에 "· Written by AutoCalcHub Team" 바이라인, **블로그+툴 전체**에 BreadcrumbList JSON-LD. FAQPage/HowTo는 2026-05-07 리치리절트 폐지로 추가 금지.

### 사이트 구조 관련 중요 변경사항
- **헤더 내비게이션**: 기존 "Calculators"/"Blog" 드롭다운 메뉴 → **단순 링크**로 전환. "Calculators" 명칭도 **"Tools"**로 변경됨. **7/17 세션에서 "Glossary" 항목 추가** — 현재 Tools / Blog / Glossary / About 4개. (`assets/partials/header.html`)
- **"← All tools" 백링크**: `assets/js/components.js`에서 관리, `tools/index.html`로 연결됨 (예전엔 홈페이지 `#tools` 앵커였는데 수정함). 툴 목록 페이지 자체에서는 이 링크가 안 뜨도록 처리돼 있음.
- 모든 페이지는 `assets/partials/header.html`, `footer.html`을 JS(`components.js`)로 fetch해서 공유 렌더링 — 헤더/푸터는 한 곳만 고치면 전체 사이트에 반영됨.
- footer에 `methodology.html`, `editorial-policy.html` 링크 상시 노출 중 (전체 페이지 공통).

## 3. 작업 규칙 (반드시 지킬 것)
1. **지시 있을 때만 작업, 먼저 진행하지 않음**
2. **작업 전 항상 저장소 최신 상태 확인 후 진행** (GitHub 토큰을 그때그때 받아서 clone/pull — 토큰은 작업 후 사용자가 즉시 revoke하는 방식으로 운영 중. 매번 새로 받아야 함)
3. **완료 후 GitHub에 직접 commit & push** (변경분 커밋 메시지에 상세 내역 기록)
4. **새 콘텐츠(블로그/툴) 작성 전 반드시:**
   - 기존 블로그/툴 전체와 중복 여부 확인 (`ls blog/`, `ls tools/`로 전수 대조)
   - 웹 검색으로 경쟁 강도 확인 — NerdWallet/Bankrate/Edmunds/ConsumerReports/보험사(Progressive·GEICO·Allstate)급이 상위 독점하면 피하고, 소형 계산기 사이트(carcalcpro.com, calculator.me 등)가 섞여서 나오면 기회로 판단
   - 신규 툴은 기존 툴과 **계산 로직 자체가 겹치지 않는지** 반드시 확인 (예: negative-equity-rollover-calculator는 gap-insurance-calculator와 달리 "롤인 시 새 대출에 미치는 영향"에 특화해서 차별화함)
   - 키워드 방향을 먼저 보고하고 확인받은 후 작성 시작
5. **콘텐츠 보강 시 공통으로 같이 처리해야 하는 것** (절대 빠뜨리지 말 것):
   - 해당 파일의 `dateModified` (JSON-LD) 최신 날짜로 업데이트
   - `blog-meta` 표시 (예: "10 min read · Updated July 2026") — 블로그만 해당, 툴 페이지는 없음
   - Related Guides 섹션 추가/보강 (내부링크 3~5개) — 툴/블로그 전부 필수
   - `blog/index.html`의 Latest 섹션 + 해당 카테고리 섹션 둘 다 업데이트 (Updated/New 배지 포함)
   - `index.html`의 메인 블로그 미리보기 섹션 (최신순 3개 유지)
   - 신규 페이지인 경우 추가로: `sitemap.xml`(신규 URL + lastmod), `llms.txt`, (툴이면) `index.html`의 tools 그리드 카드 + stat 숫자(현재 "21+") + `tools/index.html`, (블로그면) `blog/index.html` 해당 카테고리 섹션
6. **CTR이 낮은데 순위가 괜찮은 페이지는 본문 보강이 아니라 메타(title/description) 우선 점검** — 단, 노출수 자체가 10~20회 이하로 표본이 작으면 클릭 0인 게 통계적으로 정상일 수 있으니 성급하게 메타를 고치지 말 것 (7/12 세션에서 이 이유로 작업 보류한 사례 있음)
7. **작업 완료 후 반드시 검증**: div 태그 밸런스, JSON-LD 유효성, sitemap XML 유효성, 내부링크 실존 여부를 스크립트로 재확인 후 커밋. (특히 str_replace로 CTA 박스나 섹션 헤딩을 편집할 때 old_str/new_str 경계에서 태그를 통째로 날려먹는 실수가 반복적으로 발생했음 — 편집 직후 grep으로 즉시 재확인하는 습관 필요)
8. **대시보드나 시각화 자료는 만들지 말 것** (요청 시) — 분석 결과는 텍스트로만 전달
9. **작업할 게 없으면 억지로 만들지 말 것** — 노출/클릭 데이터가 통계적으로 무의미한 수준(표본 수십 건 이하)이면 "오늘은 작업 없음"이라고 솔직하게 보고하는 게 맞음. 신규 콘텐츠를 무리하게 늘리면 크롤링 예산만 분산됨.
10. **E-E-A-T/저자 신뢰도 작업 시 허위 경력·자격증 절대 지어내지 말 것** — "재무설계사 자격증을 가진 아무개" 같은 가짜 프로필은 Google 스팸 정책 위반이며 발각 시 페널티 리스크가 큼. 저자는 "AutoCalcHub Team"으로 익명 유지하고, 대신 방법론 투명성(`methodology.html`)·에디토리얼 정책(`editorial-policy.html`)·출처 표기 등 **조직 차원의 진짜 신뢰 신호**로 보강할 것.
11. **지금 바로 할 수 있는 작업을 "나중에"로 미루지 말 것** (8/7 세션에서 사용자가 직접 지적). 향후 필요할 걸 알고 있는 문구/정책 수정처럼 리스크 없이 지금 처리 가능한 항목은 "다음에 하겠다"고 보고만 하지 말고 그 자리에서 실행할 것. **공격적 확장 기조가 기본값** — 색인/트래픽이 더디다는 이유로 발행 속도나 작업 범위를 스스로 줄이자고 제안하지 말 것 (8/7 세션에서 이 방향 제안이 명시적으로 기각됨, 6-12 참고).

## 4. 주간 루틴 (정기 작업, 일요일)
- 매주 일요일: 블로그 3개 + 툴 1개 **신규 또는 보강**
- 작업 시작 전 GA4 + Search Console 리포트 캡처 받아서 방향 잡기
- **정기 루틴과 별개로**, 세션 여유가 있을 때 GSC 데이터 기반 추가 보강/신규 작업을 하기도 함 (7/8, 7/10 세션이 이 케이스) — 이건 "주간 루틴 소진"과 무관하게 별도로 카운트됨

## 5. SEO / Search Console 현황 (2026-09-07 확인, 자료는 8/24자 GSC 3종 + GA4 + Bing 2종)

### 🚨 발견 1 — 구글 노출 1,750→106 폭락은 "5월 스파이크의 윈도우 이탈"이지 순위 하락이 아니다
- 3개월 롤링 윈도우 동일 조건에서 노출 1,750(8/11) → 1,319(8/18) → **106(8/24)**. 92% 급감.
- 원인 규명: **8/11 스냅샷의 노출이 2026-05-12~21 열흘에 집중**(271+256+239+231+229+218+97+47+43+33 ≈ 1,664 / 1,750). 이 구간이 롤링 윈도우 밖으로 나가면서 통째로 빠짐.
- 그 스파이크는 거의 전부 `car-insurance-estimator`가 **85위권에서 받은 노출**이라 CTR 0이었음 → **실수요가 아니라 초기 크롤/디스커버리 버스트**.
- **결론: 우리 사이트의 "1,700 노출"은 처음부터 허수였다.** 진짜 구글 오가닉 실체는 **일 0~5노출**. 이 판단을 다음 세션들이 유지할 것.

### ✅ 발견 2 — 스파이크가 걷히자 진짜 순위가 드러났고, 훨씬 좋다
5월 스파이크(전 페이지 75~90위)가 평균을 끌어내리고 있었음. 8/18 → 8/24 평균순위 변화:

| 페이지 | 8/18 | 8/24 |
|---|---|---|
| tools/fuel-cost-calculator | 39.5위 | **5.29위** |
| tools/car-depreciation-calculator | 58.2위 | **7.00위** |
| tools/ev-charging-cost-calculator | 39.8위 | **7.62위** |
| tools/gas-vs-ev-savings-calculator | 50.2위 | **8.67위** |
| tools/car-loan-calculator | 4.2위 | **4.18위** |
| tools/car-insurance-estimator | 86.0위 | **19.5위** |
| glossary/ | 2.0위 | **3.67위** |

→ **구글에서 툴 페이지들은 이미 한 자릿수~10위권.** 문제는 순위가 아니라 (a) 색인된 페이지가 19개뿐 (b) 해당 쿼리들의 절대 검색량이 극히 낮음.

### 🎉 발견 3 — Bing에서 사이트 최초의 진짜 오가닉 클릭 2건
- Bing 노출 **55(8/18) → 415(8/24), 7.5배 폭증.** 클릭 0 → **2**.
- `how-much-should-i-put-down-on-a-car` 44노출/**1클릭**/5.73위 — 쿼리 "if im buying a 47k car, what should i put down?/" 2위
- `electric-vs-gas-car-true-cost` 9노출/**1클릭**/13.67위 — 쿼리 "what is the average cost increase for a full electric car over a non-electric car same model" 1위
- **한국발 브랜드검색을 제외한 최초의 실제 오가닉 클릭.** 초장꼬리 전략이 Bing에서 작동한다는 첫 증거.

### 📌 발견 4 — MPG 페이지: 최대 자산인데 CTR 0 (이번 세션 최우선 작업 근거)
- `what-is-a-good-mpg-for-a-car` **235노출(Bing 전체의 57%) / 5.48위 / 클릭 0**. 8/18 89노출 → 235노출로 2.6배 성장.
- 같은 5.7위인 put-down 페이지는 44노출로 1클릭을 냈는데 이쪽은 235노출로 0클릭 → **순위 문제가 아니라 메타 문제**로 확정.
- 원인 특정: **Bing 최다 쿼리가 "what is the average mpg for a car"(14노출)인데 8/18 타이틀에 "average"가 없었음.**
- 숫자 진입 쿼리가 8/18 대비 크게 확산: 23·29·30·32·35·36·38·39.2·40·43·49·60·223 등. 우리 룩업 표에 **29/32/36/43/49가 없었음.**

### 구글 쿼리 신호 (8/24, 39개)
- **`car refinance pre approval` 3.33위 유지**(3노출) — 리파이낸스 제휴(단가 최상위) 의도 쿼리.
- **`car break even calculator` 5노출**(최다 쿼리) / 88.6위, `car savings calculator` 4노출/94.75위 — "손익분기/절약" 프레임 수요.
- **running/expense calculator 군집 7개**: car running costs / used car running cost / running cost of car / car expense / auto expense / vehicle expense / car allowance calculator (84~100위). 서빙 페이지가 애매함 → **`car-total-cost-of-ownership-calculator` 최적화 여지**(다음 세션 후보).
- **`excess mileage charge calculator` 85위** — 전용 페이지 0개였음 → 이번 세션 신규로 대응.

### GA4 (7/27~8/23)
- 활성 사용자 73명, **참여시간 19.6초 → 29.0초로 회복**(3세션 만에 반등).
- 세션 소스: (direct) 48, **bing organic 10**, claude.ai 5, yahoo 5, duckduckgo 4. **google organic이 목록에서 사라짐(0).**
- 조회수 상위: 홈 25 → **MPG 13 → put-down 9 → ship-vs-drive 7**. 8/31 신규 툴이 벌써 4위.

### 📌 전략적 결론 (9/7 갱신)
1. **구글 병목은 여전히 크롤링**(미색인 91개 전부 최종크롤링 1970-01-01 = 미크롤링). 색인 19개 정지.
2. **하지만 구글에서 색인된 페이지의 순위는 이미 좋다**(5~9위권). 신규 발행보다 **색인된 19개 페이지의 쿼리 커버리지를 넓히는 편**이 구글 쪽에서는 효율이 높음.
3. **Bing이 실질 채널이고 성장 중**(55→415노출, 첫 클릭 2건). **Bing KeywordReport가 가장 실용적인 키워드 소스** — 매 세션 우선 분석할 것.
4. **CTR 최적화가 검증된 트랙이 됨.** 순위는 이미 좋으므로 메타만 맞으면 클릭이 난다(put-down이 증명). MPG 페이지 메타를 이번에 "average" 포함으로 재교체했으니 **다음 세션에서 효과 확인 필수.**
5. **🚫 "GSC 색인 생성 요청 수동 제출" 제안 금지** (8/11 사용자 명시 기각). 사이트맵 경로가 더 나았음.
6. 노출 급감을 "순위 하락/패널티"로 오독하지 말 것 — 롤링 윈도우 아티팩트임이 이번에 규명됨.

## 5-1. 수익화 정책 (2026-08-07 사용자 지시로 확정 — 이후 세션 전부 이 기준 적용)

### 기본 방침
- **우리는 구글 애드센스에 의존하지 않는다.** 애드센스는 여러 수익화 옵션 중 하나일 뿐이며, 우선순위가 높은 것도 아니다.
- **수익이 되는 제휴/광고는 종류를 가리지 않고 다 한다.** 제휴 마케팅, 광고 네트워크, 리드젠, 스폰서십 등 전부 검토 대상.
- **애드센스 게시 탈락 시 재심사 여부는 Opus가 판단한다.** 자동으로 재심사를 넣지 말고, 재심사 비용(시간·콘텐츠 수정 부담) 대비 실익을 따져서 판단할 것. 다른 제휴사·광고사도 마찬가지로 가입/유지/철수를 판단할 것.
- **애드센스보다 다른 제휴/광고가 이득이라고 판단되면 그 방향을 사용자에게 추천할 것.** 기존에 애드센스를 깔아놨다는 이유로 관성적으로 유지하지 말 것.

### 현재 인프라 상태 (8/7 기준 확인)
- `index.html` 등에 애드센스 스크립트(`ca-pub-5592663499707350`) 1줄 삽입돼 있으나, **실제 광고 유닛은 하나도 배치돼 있지 않음.** 페이지의 `<div class="ad-banner">Advertisement · Google AdSense</div>`는 전부 **플레이스홀더 텍스트일 뿐 실제 광고가 아님.** 즉 현재 사이트 수익은 구조적으로 $0이며, 애드센스 승인 여부와 무관하게 그렇다.
- 7/13 애드센스 "가치가 별로 없는 콘텐츠" 정책 위반 → 재심사 제출 후 **결과 미확인 상태가 3주 이상 지속 중.**
- `editorial-policy.html`에 현재 "제휴 마케팅을 하지 않는다"고 명시돼 있음 → **제휴 도입 시 이 문구를 반드시 먼저 수정해야 함**(안 고치면 자기모순 + 신뢰도 훼손). 동시에 FTC 제휴 고지 문구를 해당 페이지들에 넣어야 함.

### 수익모델 판단 근거 (8/7 리서치)
- 오토 파이낸스 제휴 단가(웹서치 확인): 오토 리파이낸스 성사당 $60~150, LendingTree 리드당 최대 $70, myAutoloan 신청당 $4~15(볼륨 티어), 서브프라임 리드젠은 리드당 $300까지도 있음.
- **애드센스는 세션당 몇 센트 수준이라 월 수천~수만 방문이 있어야 의미가 생김. 반면 제휴는 "고의도 방문자 100명"이 "일반 방문자 5,000명"보다 나을 수 있음.** 우리 사이트의 초장꼬리 전략은 필연적으로 저볼륨·고의도 트래픽을 만들기 때문에 **구조적으로 제휴 쪽이 궁합이 맞음.**
- 단, **트래픽이 0이면 제휴도 $0이다.** 제휴 전환은 수익모델 문제가 아니라 여전히 색인/권위 문제 뒤에 있음 — 제휴 세팅 자체를 서두를 이유는 없고, 트래픽이 붙기 시작하는 시점에 맞춰 준비하면 됨.

### 권장 우선순위 (Opus 판단, 8/7)
1. **애드센스 재심사는 지금 넣지 말 것.** 색인 21% 상태에서 재심사를 넣으면 "가치가 별로 없는 콘텐츠" 판정이 반복될 가능성이 높고, 승인돼도 현재 트래픽에선 월 $0~1 수준이라 실익이 없음. 색인률과 오가닉 트래픽이 의미 있게 올라온 뒤에 재검토.
2. **제휴는 트래픽이 붙은 뒤 도입.** 다만 어떤 프로그램을 쓸지는 미리 정해둘 가치 있음 — 우선 후보: 오토 리파이낸스(Caribou, RefiJet — 단가 최상위), 오토론 마켓플레이스(myAutoloan, LendingTree), 중고차 인스턴트 오퍼(Peddle, CarMax), 연장보증(Endurance, CarShield). **대부분 최소 트래픽 요건이 있어서 지금 신청하면 거절될 수 있으니 서두르지 말 것.**
3. **보험 제휴는 단가가 가장 높지만(리드당 $10~50) 우리 보험 페이지가 85위라 현실성 없음** — 보험 방치 정책과 동일하게 판단.

## 6. 이번 대화 세션들에서 진행한 작업 전체 이력

### 6/29 세션 이전 (이전 세션 요약, 원본 인수인계 문서 기준)
- 6/22: 색인 문제 대응으로 툴 9개 + 블로그 7개 콘텐츠 보강 (단어수 부족이 원인)
- 6/29: 신규 5개(툴3+블로그2), 콘텐츠 보강 7개, 메타 CTR 개선 2개, blog/index.html·index.html·sitemap.xml·llms.txt 갱신

### 7/4 세션: 표 반응형 수정 + is-72-month/car-affordability 차별화
- Search Console에서 색인 미생성 47개 확인 → 재조사 결과 `is-72-month-car-loan-bad-idea.html`, `tools/car-affordability-calculator.html`가 사이트 내 다른 페이지(GAP보험, 20/4/10 규칙 등)와 콘텐츠 중복(캐니벌라이제이션)되어 있던 게 색인 안 되는 원인으로 판단 → 중복 섹션 제거하고 고유 앵글로 교체
- 단어수 부족 7개(블로그2+툴5) 보강, sitemap lastmod 전체 추가
- **표(`<table>`) 반응형 처리 누락 발견** → 표 있는 블로그 30개 전체에 `.table-wrap`(overflow-x:auto) + 모바일 미디어쿼리 일괄 적용

### 7/6 세션: GitHub 토큰 직접 작업 방식 시작 + Negative Equity 클러스터 (주간 루틴)
- 이때부터 **사용자가 GitHub PAT를 직접 발급해서 주고, 작업 완료 후 즉시 revoke하는 방식**으로 전환됨. 매 세션 토큰을 새로 받아야 함.
- 헤더 내비게이션 드롭다운 → 링크 전환, Calculators→Tools 명칭 변경, `tools/index.html` 신규 생성 (이번 문서 2장 참고)
- 신규 툴: **Negative Equity Rollover Calculator** (기존 gap-insurance-calculator와 차별화 — "롤인 시 새 대출 영향"에 특화)
- 신규 블로그 3개: "What Is Negative Equity on a Car Loan?", "Should You Roll Negative Equity Into a New Car Loan?", "What Is Loan-to-Value (LTV) Ratio?"

### 7/8 세션: 사이트 전체 콘텐츠 기초체력 진단 및 보강 (주간 루틴과 별개)
- 노출수 급감 이슈로 전체 39블로그+20툴 전수 스캔 진행
- **Related Guides 섹션이 아예 없던 페이지 7개** 발견 → 신설 + 단어수 보강 (블로그 6개 + 툴 1개)
- **JSON-LD에 dateModified 필드가 아예 없던 툴 12개** 발견 → 전체 추가
- Related Guides가 2~3개로 얕던 툴 4개 → 4~5개로 보강
- blog/index.html, sitemap.xml(17개 lastmod 갱신) 반영

### 7/10 세션: 금리표 리프레시 + Bi-Weekly 클러스터 (주간 루틴과 별개, "업그레이드" 성격)
- Search Console 키워드 데이터에서 "auto loan rates 2026 by credit tier" 계열이 이미 17~20위로 잘 나오는 걸 확인 → `what-is-good-interest-rate-car-loan.html`의 금리표를 Experian Q4 2025 기준 신용등급 구간으로 리프레시 + 출처 명시
- 웹 검색으로 "bi-weekly car payment calculator" 키워드가 대형 사이트 없이 소형 계산기 사이트들만 상위권인 걸 확인 → 신규 클러스터로 결정
- 신규 툴: **Bi-Weekly Car Payment Calculator** (기존 car-early-payoff-calculator와 메커니즘 다르게 차별화 — 목돈 추가납입 vs 격주납 전환)
- 신규 블로그 2개: "Bi-Weekly vs Monthly Car Payments", "How to Set Up Bi-Weekly Car Payments With Your Lender" (3번째 블로그는 억지로 안 채우고 2개로 마무리 — "확실한 것만 하고 없으면 스톱" 원칙 적용)

### 7/12 세션 (1차): GSC 데이터 재확인, 작업 없음으로 결론
- Performance + Coverage 리포트 확인. Coverage는 6/30 데이터까지만 반영(지연), Performance는 7/10 세션과 거의 동일한 패턴(노출 여전히 하루 0~4건, 신규 콘텐츠는 아직 노출 0건 — 정상적으로 너무 이름)
- **신규 이슈 2건 조사**: "리디렉션 포함 페이지(실패함)" 1건, "적절한 표준 태그 대체 페이지" 1건 → 코드 전체 검증(http:// 하드코딩, www. 절대경로, 잘못된 canonical) 결과 전부 없음 확인 → **호스팅 레벨(Cloudflare/GitHub Pages)의 정상적인 http→https 리디렉션으로 판단, 코드 수정 불필요**
- 수익화(AdSense) 관점에서 냉정하게 판단: 3개월 누적 클릭 0건인 상황에서 신규 콘텐츠를 더 만들어도 단기 매출 영향 없음 → **오늘은 작업 없음으로 결론**, 억지로 일 만들지 않음

### 7/12 세션 (2차): E-E-A-T 개선 (장기 레버 관점)
- "장기적으로 추가할만한 것" 질문에서 시작 — 백링크(이미 어느정도 있음, 우선순위 아님), FAQPage/HowTo 스키마(0% 사용 중, 다음 후보), **E-E-A-T 저자 신뢰도 부재**(3가지 중 최우선으로 결정) 발견
- 원칙: **허위 경력/자격증 절대 지어내지 않음** (스팸 정책 위반 리스크). "AutoCalcHub Team"으로 익명 유지, 대신 조직 차원 투명성/전문성 신호로 보강
- **신규 페이지 2개**: `methodology.html`(계산 공식·가정·데이터 출처 전체 공개, Experian/Bankrate/Edmunds/EIA/KBB 명시), `editorial-policy.html`(콘텐츠 제작/검수 기준, 광고-콘텐츠 분리 원칙, 제휴 관계 없음 명시, 정정 정책)
- footer.html에 두 페이지 링크 추가 (전체 페이지에 자동 반영) + 오래된 저작권 연도(2025→2026) 수정
- about.html에도 상호 링크 추가
- **블로그 44개 전체**에 안전한 정규식 일괄 처리로 "· Written by AutoCalcHub Team" 바이라인을 기존 blog-meta 줄에 통합 (str_replace 개별 편집 대신 python 스크립트로 일괄 처리 — 44개 파일 각각 blog-meta div가 정확히 1개씩인지 사전 확인 후 처리, 태그 유실 리스크 회피)
- **`car-insurance-estimator.html`(사이트 내 노출 1위, 1,074회) 보험료 평균치 갱신**: $1,700-2,100 → $2,200-2,600 (2026년 최신 데이터, U.S. News/ValuePenguin 출처 명시) — 방치 정책 유지하되 정확성/신뢰도는 유지
- sitemap.xml(+2 URL, 73개), llms.txt("About This Site" 섹션 신규) 반영
- 커밋 `31ee7fc`, 51개 파일

### 7/12 세션 (3차): E-E-A-T 나머지 작업 — BreadcrumbList 스키마 + 출처 보강
- **중요 정정**: 웹 검색 결과 Google이 2026-05-07에 FAQ 리치 리절트를 완전히 폐지한 것 확인 (HowTo는 2023년에 이미 폐지). 2차 세션에서 "FAQ/HowTo 스키마 = CTR 개선 레버"라고 안내한 게 최신 정보 기준 틀림 → **FAQ/HowTo 스키마 작업 후보에서 제외**
- 대신 **BreadcrumbList 스키마**로 대체 진행 — Google이 여전히 지원하고 모바일 CTR 5~10% 개선 효과가 있다고 알려진 타입인데 사이트 전체 사용률 0%였음
- **블로그 44개 + 툴 21개 = 65개 페이지 전체**에 BreadcrumbList JSON-LD 일괄 삽입 (Home > Blog/Tools > 페이지명, 각 페이지 기존 canonical URL/title 재사용, python 스크립트로 안전하게 일괄 처리 후 130개 JSON-LD 블록 전체 유효성 검증)
- `tools/car-depreciation-calculator.html`의 "연간 15-25% 감가" 통계에 출처(KBB/Edmunds/iSeeCars) 추가
- `tools/car-maintenance-cost-calculator.html`은 이미 RepairPal/AAA 출처 명시돼 있어서 손 안 댐
- 커밋 `fa60353`, 66개 파일

### 7/13 세션: AdSense "가치가 별로 없는 콘텐츠" 정책 위반 대응 (전체 사이트 콘텐츠 점검)
- **트리거**: 7/11 AdSense가 사이트를 "가치가 별로 없는 콘텐츠(low value content)"로 플래그. 스크린샷 확인 후 즉시 전체 사이트 점검 지시받음.
- **진단**: 65개 페이지(블로그44+툴21) 전수 단어수 스캔. 블로그는 전부 900~2,400단어로 양호. **툴 21개 중 11개가 800단어 미만**으로 확인 — 특히 `car-loan-calculator.html`(사이트 내 순위 1위, 4.07위, 트래픽 최상위)이 317단어로 최악. 계산기 위젯 + 짧은 설명 3~4문단짜리 "실속 없는 유틸리티 페이지" 패턴이 원인으로 판단. 광고 밀도·중복 콘텐츠는 스캔 결과 문제 없음으로 배제.
- **조치**: 800단어 미만 툴 11개 전부를 900~1,040단어 수준으로 보강 (계산 공식/방법론 설명, 실제 숫자로 계산한 예시, 흔한 실수, 트레이드인/세금/신용점수 영향 등 엣지케이스 섹션 추가). `tools/index.html`도 인트로 문단 + 카테고리별 설명 추가 (451→650단어).
  - car-loan-calculator.html: 317 → 1042
  - car-early-payoff-calculator.html: 513 → 826
  - car-refinance-calculator.html: 514 → 807
  - car-total-cost-of-ownership-calculator.html: 587 → 940
  - car-down-payment-calculator.html: 621 → 940
  - car-trade-in-value-estimator.html: 662 → 919
  - gap-insurance-calculator.html: 664 → 945
  - biweekly-car-payment-calculator.html: 673 → 916
  - car-maintenance-cost-calculator.html: 679 → 885
  - fuel-cost-calculator.html: 746 → 971
  - negative-equity-rollover-calculator.html: 774 → 1011
- **부수적으로 발견한 오류 수정**: 콘텐츠 보강 과정에서 기존 예시 수치들을 실제 상환 공식으로 재검증하다가 오류 2건 발견해 수정함 — `car-refinance-calculator.html`(월 $80/총이자 $3,800 절감이라고 써있었는데 실제 계산은 월 $38/총이자 $1,800), `car-down-payment-calculator.html`(총이자 $2,400 절감이라고 써있었는데 실제는 $1,200). 새로 추가한 예시 수치도 전부 파이썬으로 실제 상환 공식 검증 후 게재.
- **검증**: 12개 파일 전체 div 태그 밸런스, JSON-LD 유효성, 내부링크 실존 여부를 스크립트로 확인 후 커밋 (작업 중 gap-insurance-calculator.html에서 str_replace로 닫는 div 하나가 실제로 유실되는 사고 발생 → 즉시 재확인 습관 덕분에 커밋 전 잡아냄, 규칙 7의 사례 재확인됨).
- sitemap.xml 12개 URL lastmod 갱신, dateModified(JSON-LD) 12개 파일 전체 갱신.
- 커밋 `6a38ed2`, 13개 파일. **결과: 800단어 미만 페이지 11개 → 0개, 사이트 전체 최저 단어수 807단어.**
- footer-links 반응형 오버플로우 버그도 같은 세션에서 추가로 발견/수정 (`flex-wrap` 누락, 커밋 `9107cd4`) — 콘텐츠 이슈와 무관한 별개 CSS 버그.
- **7/13 사용자가 AdSense 재검토(검토 요청) 버튼 직접 제출함 — 현재 심사 대기 중.** 심사 결과 나올 때까지 통상 며칠~1-2주 소요.

### 7/13 세션에서 갱신된 콘텐츠 볼륨 기준
- 65개 페이지 전체 800단어 이상. 블로그 900~2,442단어, 툴 807~1,163단어.
- 신규 툴/블로그 작성 시 최소 800단어, 가급적 900단어 이상을 목표로 할 것 (7/13 사건 이후 새 기준).

### 7/15 세션: 색인 미생성 원인 진단 + 내부링크 구조 보강 (AdSense 재검토 대기 중, 신규 콘텐츠 없이 진행)
- **AdSense 재검토 여전히 대기 중** (7/13 제출, 결과 안 나옴). 이번 세션 시작 시점 기준 상태 미확인 — 다음 세션 시작 시 먼저 확인할 것.
- **트리거**: 최신 GSC 리포트(7/15) 확인 결과 sitemap 73개 URL 중 실제 색인 16개, 미색인 55개("발견됨-크롤링대기" 53 + "크롤링됨-미생성" 2)로 지난 세션(7/12, 47개) 대비 오히려 악화. "새 도메인이라 정상"이라는 기존 결론을 재검증하라는 지시에 따라 원점에서 재조사.
- **재조사 방법**: sitemap 73개 vs GSC Performance에서 노출 1회 이상 있었던 16개 URL을 대조해 미색인 55개(정적 페이지 제외 시 블로그 24개 + 툴 다수)의 실제 목록을 확보. 이후 각 페이지의 git 최초 커밋일을 대조해 "아직 크롤링 대기 중이라 정상"인 케이스(7/6·7/10 게시분)와 "8~9주 지난 구관인데도 미색인"인 케이스(5/11~5/26 게시분, 이게 다수)를 분리.
- **가설 검증 1 — 템플릿/스팸성 중복 콘텐츠 여부**: 미색인 블로그 44개 전체의 도입부 문단을 전수 대조. 전부 서로 다른 통계·다른 서두로 작성돼 있어 find-replace형 양산 콘텐츠 패턴 없음 확인. 이 방향은 배제.
- **가설 검증 2 — 기술적 차단 여부**: robots.txt(Allow: / 정상), noindex 메타 태그(전체 없음), canonical 태그(전 페이지 자기 자신 참조, 중복 없음) 전수 확인 — 문제 없음. 7/12에 확인된 리디렉션 1건·대체 캐노니컬 1건은 호스팅 레벨 이슈로 재차 배제.
- **가설 검증 3 (채택) — 색인된 페이지로부터의 내부링크 결손**: 전체 사이트 73개 페이지의 href를 상대경로까지 정확히 정규화해서 "이미 색인된 16개 페이지"가 각 미색인 페이지로 몇 개의 링크를 보내는지 전수 계산. 결과: **색인된 페이지로부터 링크를 0개 받는 페이지 9개는 예외 없이 100% 미색인**. 반대로 3개 이상 받는 페이지는 대부분 색인됨. 이 상관관계는 웹서치로 교차 검증한 2026년 기준 최신 SEO 자료(Search Engine Journal의 John Mueller 인용 포함)와도 일치 — "이미 색인된 고권위 페이지發 contextual 내부링크가 discovered-currently-not-indexed 해소의 가장 확실한 레버"라는 게 정설로 재확인됨.
- **결론 및 조치**: 신규 콘텐츠 작성은 보류(크롤 신뢰만 더 분산시키는 역효과 우려, rule 9 적용). 대신 색인된 허브 페이지 7개(`car-loan-calculator`, `car-down-payment-calculator`, `how-much-car-can-i-afford`, `how-to-get-pre-approved-car-loan`, `what-is-good-interest-rate-car-loan`, `used-car-value-calculator`, `car-depreciation-calculator`)의 Related Guides 섹션에, 링크 0개였던 미색인 페이지 9개(`what-is-a-good-car-payment-per-month`, `how-to-get-out-of-a-car-lease-early`, `what-happens-when-car-loan-is-paid-off`, `how-long-does-it-take-to-pay-off-car-loan`, `how-much-does-car-maintenance-cost-per-year`, `what-is-cheapest-car-to-maintain`, `how-to-sell-car-privately-vs-trade-in`, `should-i-buy-or-lease-a-car`, `should-you-roll-negative-equity-into-a-new-car-loan`)를 주제 관련성 기준으로 배분 삽입. 9개 중 7개는 색인된 페이지로부터 2개씩, 2개는 1개씩 링크를 받도록 처리(작업 후 스크립트로 재검증 완료).
- **검증**: 7개 파일 전체 div/li 태그 밸런스 확인, JSON-LD 유효성 확인, 신규 삽입 링크 9개 전부 실제 파일 존재 확인(깨진 링크 없음), sitemap.xml XML 유효성 확인 완료.
- dateModified(JSON-LD) 7개 파일 갱신(2026-07-15), sitemap.xml 7개 URL lastmod 갱신.
- 커밋 `(해시는 push 후 기록)` — 7개 파일 변경.
- **⚠️ 다음 세션 필독**:
  1. AdSense 재검토 결과 먼저 확인.
  2. **(최종) 미색인 페이지 55개(정적 페이지 제외 50개) 전수 처리 완료.** 1차(0링크 9개) → 2차(1링크 23개 중 18개) → 3차(남은 1링크 5개, 자연스러운 연결점 재발굴해서 전부 처리) 순으로 3차례 반복 보강. **최종 결과: 미색인 50개 전부 색인된 페이지로부터 2개 이상 내부링크 확보(2개 41개, 3개 5개, 4개 4개), 0개·1개 링크는 0개.** 링크 실존 여부·중복 여부·태그 밸런스·JSON-LD 전부 스크립트로 최종 재검증 완료, 깨진 링크 없음.
  3. **재점검 과정에서 헛다리짚을 뻔한 사례**: `car-lease-vs-buy-calculator.html`을 246단어로 잘못 측정해서 "이것도 원인인가" 싶었는데, 추출 스크립트 버그였고 실제로는 1005단어로 정상이었음(재확인 후 폐기). 콘텐츠 분량 자체는 사이트 전체에서 문제 없는 것으로 재확인(최저 824단어).
  4. 이번 조치의 효과가 1~2주 후 Coverage 리포트에 반영되는지 다음 세션에서 먼저 확인할 것. 효과가 있으면(색인 개수 16→상승) 이 방법론이 확정되는 것이고, 효과가 없으면 "내부링크 결손" 가설도 기각하고 원점 재검토 필요.
  5. Related Guides 리스트에 항목을 추가할 때는 사이드바 리스트 삽입 방식(이번 세션)보다 본문 내 contextual 링크가 이론상 더 강한 시그널이라는 점 참고 — 리스트 삽입으로 효과가 부족하면 다음 단계로 본문 내 링크 삽입 고려.
  6. `car-loan-calculator.html`의 Related Guides가 이번 세션 두 차례 보강으로 8개→14개까지 늘어남 — 사이트 평균(5~8개)보다 확연히 김. 다음 세션에서 시각적으로 리스트가 과하게 길어 보이지 않는지 한 번 확인할 것(기능상 문제는 없으나 UX 관점에서 카드형 레이아웃으로 리팩터링을 고려할 수도 있음). `how-much-car-can-i-afford.html`(8→11), `tools/car-down-payment-calculator.html`(5→9), `tools/used-car-value-calculator.html`(5→10)도 같은 이유로 늘어났음 — 다음 세션에서 시각 확인 권장.

## 6-1. 7/17 세션: 색인 진행상황 확인(아직 미반영) + 롱테일 금리 쿼리 보강
- **AdSense 재검토 결과 여전히 미확인** — 이번 세션에서도 확인 안 됨, 다음 세션 시작 시 최우선으로 확인할 것.
- **Coverage 데이터**: 7/17 리포트도 7/10 데이터까지만 반영(항상 있는 1~2주 지연). 색인 16개/미색인 55개 그대로 — **7/15 내부링크 보강의 효과는 이번에도 판단 불가**. 최소 다음다음 세션(1~2주 후) 확인 필요.
- **Performance 데이터**: 여전히 16개 페이지, 클릭 0건 유지. 통계적으로 무의미한 수준 그대로(규칙 9).
- **신규 발견 — 쿼리 레벨 분석에서 롱테일 기회 확인**: "best/average car loan rates 2026 (excellent/good/strong/great credit)" 계열 쿼리 7개가 전부 17~20위(2페이지 끝, "거의 다 온" 구간)에 몰려있음. 담당 페이지는 `what-is-good-interest-rate-car-loan.html`.
- **원인 진단**: 웹서치로 Experian 원본 리포트 재확인 결과, 페이지가 Q4 2025 range 데이터("4.5-6.0%" 식)를 쓰고 있었고, 검색어에 실제로 쓰이는 "excellent/good/strong/fair credit" 같은 일상 표현이 페이지엔 "Super Prime/Prime" 전문용어로만 존재 — 검색 의도와 미세하게 어긋나 있었음. 경쟁 강도 자체는 Experian/Bankrate/LendingTree/U.S.News/Credit Karma급 대형 사이트가 많이 나오지만(보험 카테고리처럼 완전 독점은 아님), otdcheck.com/caralpha.org 같은 소형 사이트도 섞여서 상위권에 있는 걸 확인 — 완전히 승산 없는 영역은 아니라고 판단.
- **조치**: 신규 콘텐츠 대신 기존 페이지 보강 선택(7/15 내부링크 작업 이틀밖에 안 지나서 크롤 신뢰 회복 중인데 새 페이지 만들면 크롤 예산 분산 우려 — rule 9). Q1 2026 Experian 정확한 수치(Super Prime 4.55%/6.30% 등)로 표 갱신 + "everyday terms" 열 추가해서 전문용어·일상표현 병기 + 전국 평균 수치(6.39%/11.43%)도 최신화 + 상단에 "Quick answer" 콜아웃 박스 신규 추가(AI검색/스니펫 추출 대응, 기존 highlight-box 클래스 재사용해서 신규 CSS 없이 처리).
- **"car refinance pre approval" 쿼리(3.33위)는 판단 보류**: 노출 3회뿐이라 규칙 6에 따라 표본 부족으로 손대지 않음.
- **검증**: div/tr/table 태그 밸런스, JSON-LD 유효성, sitemap XML 유효성 전부 스크립트로 확인 완료. dateModified/sitemap lastmod 갱신.
- 커밋 `962af3a`, 2개 파일 (`blog/what-is-good-interest-rate-car-loan.html`, `sitemap.xml`).
- **⚠️ 다음 세션 필독**:
  1. AdSense 재검토 결과, 7/15 내부링크 보강 효과(색인 수 16→?), 이번 금리 페이지 보강 효과(17~20위→?) 전부 아직 미확인 상태 — 다음 세션에서 최소 2주 경과 후 재확인.
  2. **오늘 적용한 패턴("Quick answer" 콜아웃 + 검색어 실사용 표현 병기)은 다른 페이지에도 확장 적용할 만한 템플릿**임. 사용자가 "AI검색은 도메인 권위보단 콘텐츠 내용, 문제해결/비교분석이 유리하다"고 언급한 방향과 일치. 근거가 확실한 페이지(순위 데이터로 뒷받침되는 곳)부터 순차 확장할 것 — 65개 페이지 전체에 한 번에 적용하지 말고, 이번처럼 데이터 근거 있는 곳부터 하나씩.
  3. 이번 세션은 신규 콘텐츠 없이 종료 — 사용자가 신규도 검토해보라고 했지만, 조사 결과 새로 만들 가치가 검증된 롱테일 기회를 못 찾았고(기존 페이지들이 이미 잘 커버 중), 크롤 예산 우려도 있어서 보강으로 결론. 다음 세션에서 색인 회복이 확인되면 그때 신규 콘텐츠 재검토 여지 있음.

## 6-2. 7/17 세션(2차): 신규 콘텐츠 1건 + 미색인 페이지 콘텐츠 품질 재점검
- **사용자 피드백**: "신규 콘텐츠 너무 안 한 지 오래됐다, 롱테일 선점 필요" + "보강도 한 페이지만 하지 말고 확실하게" → 두 가지 다 대응. (바로 위 6-1 세션에서 "신규 콘텐츠 없이 종료"라고 결론 냈던 걸 사용자가 반려한 상황.)
- **미색인 페이지 콘텐츠 품질 재점검(보강 관련)**: 수익화 가치 높은 미색인 페이지 5개(`should-i-buy-or-lease-a-car`, `how-long-does-it-take-to-pay-off-car-loan`, `how-to-sell-car-privately-vs-trade-in`, `should-you-roll-negative-equity-into-a-new-car-loan`, `what-is-a-good-car-payment-per-month`) 콘텐츠 상태 전수 확인 → **전부 1,000~2,000단어, 비교표 1~2개, Side-by-Side 섹션까지 이미 갖춘 양호한 콘텐츠로 확인**. 콘텐츠 품질은 문제가 아니라는 7/15 진단이 재확인됨 — 억지로 더 손대지 않음(규칙 9, 이미 좋은 콘텐츠에 손대는 건 불필요한 리스크). **7/15에 이미 미색인 50개 전부 내부링크 보강 완료했다는 점을 사용자에게 명확히 재설명함** — 오늘 "한 페이지만" 한 건 그와 별개로 이미 색인된 페이지의 순위를 밀어올리는 다른 종류의 보강이었음.
- **신규 콘텐츠**: `blog/should-you-pay-cash-or-finance-a-car.html` — "현금 완납 vs 대출로 구매" 의사결정 가이드.
  - **중복 확인**: 기존 65개 전체 리스트 대조 결과, 리스vs구매(`should-i-buy-or-lease-a-car`)와 금리 자체(`what-is-good-interest-rate-car-loan`)는 있었지만 "현금이냐 대출이냐" 자체를 다루는 페이지는 없었음 — 진짜 갭 확인.
  - **경쟁강도 확인**: 웹서치 결과 KBB/Experian/CarEdge 같은 대형사이트와 Jalopnik/financetothetop.com 같은 중소 사이트가 섞여서 상위권 — 보험 카테고리처럼 완전 독점 구조 아님, 승산 있다고 판단.
  - **AI검색 대응 구조** (사용자가 이번에 요청한 방향): 상단 Quick answer 콜아웃 + Pros/Cons 비교표 3개 + Side-by-Side 요약표. 문제해결·비교분석 위주로 구성.
  - **수치 검증**: 모든 예시(6.39% Q1 2026 평균 신차금리로 $30k/60개월 상환, 4.0% HYSA로 5년 복리, 0% APR vs 리베이트 비교)는 파이썬으로 실제 공식 계산 후 게재. HYSA 금리는 Bankrate/Fortune 7월 데이터로 교차 확인(4-4.5% 상위권 확인 후 보수적으로 4.0% 사용).
  - 1,241단어 (900단어 이상 기준 충족).
  - **7/15 교훈 적용**: 발행 즉시 이미 색인된 페이지 3곳(홈페이지, `what-is-good-interest-rate-car-loan`, `car-down-payment-calculator`)에서 링크를 걸어서 0링크로 시작하지 않게 처리 — 다음에도 신규 페이지 만들 때 이 패턴 유지할 것.
  - 사이트 전체 반영: `blog/index.html`(Latest+Financing 섹션 둘 다), `index.html`(홈페이지 최신 3개 미리보기 갱신 — 가장 오래된 항목 하나 교체), `sitemap.xml`, `llms.txt`.
- **검증**: div/a 태그 밸런스, JSON-LD 유효성, 신규 페이지 포함 전체 내부링크 실존 여부, sitemap XML 유효성 스크립트로 전부 확인.
- 커밋 `6eeae82`, 7개 파일.
- **⚠️ 다음 세션 필독**:
  1. 이 신규 페이지도 색인 여부를 1~2주 후 확인 대상에 포함시킬 것 (다른 지표들과 함께).
  2. 사용자가 롱테일 선점을 계속 원하는 방향이므로, 색인 회복이 확인되면 다음 세션에 신규 콘텐츠 1~2개 정도 추가로 검토 — 단, 이번처럼 진짜 갭인지 매번 반드시 확인 후 진행.

## 6-3. 7/17 세션(3차): 신규 툴 1건 (사용자 지시로 경쟁 다소 있어도 진행)
- **사용자 판단**: "현금 vs 대출 계산기" 툴을 제안하면서 경쟁이 블로그보다 세다고 보고했는데, 사용자가 "롱테일 선점은 늦어질수록 불리하다"며 진행 지시 — 확인 후 바로 제작.
- **신규 툴**: `tools/cash-vs-finance-car-calculator.html` — 오늘 만든 블로그(`should-you-pay-cash-or-finance-a-car.html`)의 짝 계산기.
  - 계산 로직: 대출 상환식 + 투자 복리식을 파이썬으로 먼저 검증한 뒤 JS로 이식(기본값 시나리오 재검증 결과 블로그 글의 예시 수치와 정확히 일치 — 6.4%/4.0% 조합에서 대출+투자가 약 $1,495 유리, 12% 고금리 시나리오는 현금이 $3,410 유리). node로 JS 문법 오류 여부도 확인.
  - 804단어 (900단어 권장 기준엔 살짝 못 미치지만 800단어 하한 충족 — 계산기 위젯 비중이 큰 툴 페이지 특성상 기존 툴들도 800대 초반이 여럿 있어 정상 범위).
  - 오늘 만든 블로그와 강하게 상호링크: 블로그 "기회비용 계산" 섹션 바로 아래에 본문 내 CTA 버튼 추가(사이드바보다 강한 신호, 7/15 교훈 적용), 사이드바 Related Guides도 양쪽에 서로 추가.
  - **7/15 교훈 재적용**: 발행 즉시 색인된 페이지 3곳(홈페이지 툴 그리드, `car-down-payment-calculator`, `what-is-good-interest-rate-car-loan`)에서 링크 확보 — 0링크로 시작하지 않음.
  - 사이트 전체 반영: `tools/index.html`(Financing 섹션), `index.html`(툴 그리드 카드 추가 + "21+"→"22+" 스탯 카운터 2곳 갱신), `sitemap.xml`, `llms.txt`.
- **검증**: div/a/ul/li 태그 밸런스, JSON-LD 유효성, 사이트 전체 깨진 링크 0건, sitemap XML 유효성 전부 스크립트로 확인. JS 계산 로직은 파이썬 사전검증 + node 문법검증 이중 확인.
- 커밋 `005107b`, 8개 파일.
- **⚠️ 다음 세션 필독**:
  1. 이번 세션에서 만든 블로그 1개 + 툴 1개 모두 색인 여부를 1~2주 후 확인 대상에 포함. 사이트는 이제 블로그 45개 + 툴 22개 = 67개 페이지, sitemap 총 URL 75개.
  2. 툴 페이지 하단 "21+"였던 스탯이 "22+"로 바뀐 것도 화면 확인 대상에 포함하면 좋음(숫자만 바뀐 텍스트라 레이아웃 깨질 요소는 없음).

## 6-4. 7/17 세션(4차): 백로그 후보 2건, 같은 세션에서 바로 발행으로 전환
- 6-4 최초 버전에서는 "조사만 해두고 발행은 페이스 조절" 방침이었으나, 사용자가 "크롤 예산 걱정은 지금 사이트 규모(69페이지)엔 크게 해당 안 되는 얘기 아니냐"고 반박 — 맞는 지적이라 인정하고 **같은 세션에서 바로 발행**으로 전환. (크롤 예산 이슈는 통상 수천 페이지급 대형 사이트에 적용되는 개념이라 69페이지 사이트에는 과도한 걱정이었음.)
- **신규 블로그 2개 발행 완료**:
  - `blog/is-certified-pre-owned-worth-it.html` — CPO 프리미엄(\$1,000-3,000) 실제 상환 비교(8.77% Q1 2026 중고차 프라임 금리 기준 파이썬 검증), 1060단어. `used-car-value-calculator`, `car-trade-in-value-estimator`와 연결.
  - `blog/is-extended-car-warranty-worth-it.html` — 자가보험(self-insure) vs 워런티 구매 비교(4% APY 복리 파이썬 검증), 932단어. `car-maintenance-cost-calculator`와 연결.
  - 두 글 상호 링크 + `should-you-pay-cash-or-finance-a-car.html`과도 교차 링크(같은 세션 3차에서 만든 글).
- **7/15 교훈 재적용**: 각각 색인된 페이지 3곳에서 링크 확보(홈페이지 latest-3 미리보기 + 전용 허브 2곳씩 — CPO는 `used-car-value-calculator`/`how-to-check-car-history-before-buying`, 워런티는 `car-insurance-estimator`/`how-to-negotiate-car-price-at-dealership` — 후자는 F&I 오피스 워런티 업셀이라는 자연스러운 연결 고리로 선정).
- 사이트 전체 반영: `blog/index.html`(Latest + 각 카테고리 섹션), `index.html`(홈페이지 latest-3 전부 교체), `sitemap.xml`, `llms.txt`.
- **작업 중 실수 1건 발견·수정**: 홈페이지 latest-3 교체 편집 중 str_replace 경계 문제로 이전 3번째 카드의 잔여 마크업(고아 태그)이 남는 사고 발생 → 재검증 스크립트(div/a 태그 밸런스)로 커밋 전 즉시 발견해서 수정 (규칙 7 사례 재확인).
- **검증**: 태그밸런스/JSON-LD/사이트 전체 깨진링크 0건/sitemap 유효성/신규 페이지 참조횟수 전부 스크립트로 확인 완료.
- 커밋 `ab80787`, 10개 파일.
- **최종 결과**: 오늘 하루에 블로그 3개(cash-vs-finance, CPO, extended warranty) + 툴 1개(cash-vs-finance-calculator) 신규 발행. 사이트는 이제 블로그 47개 + 툴 22개 = 69개 페이지, sitemap 총 URL 77개.
- **⚠️ 다음 세션 필독**: 오늘 신규 발행한 4개 전부(블로그 3개+툴 1개) 색인 여부를 1~2주 후 확인 대상에 포함. 색인된 페이지 발 링크는 전부 3개씩 확보된 상태로 시작했으니, 7/15에 검증된 방법론이 맞다면 무리 없이 색인될 것으로 예상 — 안 되면 "3링크로도 부족하다"는 신호이므로 원점 재검토 필요.


## 6-5. 7/17 세션(5차): "Selling & Trade-In" 카테고리 신설 (사용자 지시, 롱테일 초기 선점)
- **배경**: 사용자가 "낱개 콘텐츠 하나 더 늘리기"가 아니라 "새 카테고리 추가"를 제안(헤더 내비게이션 얘기 아니라 블로그 태그 카테고리 얘기였음, 스크린샷으로 확인). "개수 픽스하지 말고 최대한, 100페이지도 환영"이라는 방향으로 승인.
- **카테고리 선정 근거**: 기존 블로그 태그 분포(Financing/Buying/Running Costs/Ownership/EV) 확인 결과, "판매/처분" 콘텐츠가 Buying·Ownership에 흩어져 있고 독립 카테고리가 없었음 — "내 차를 사는 것"과 "내 차를 처분하는 것"은 다른 의사결정이라 분리가 타당하다고 판단, 제안 후 승인받고 진행.
- **신규 4개 콘텐츠** (전부 웹서치로 경쟁강도 확인 + 기존 콘텐츠와 중복 확인 완료 후 작성, 900단어 내외):
  - `carmax-vs-carvana-which-pays-more.html` (957단어) — 기존 `how-to-sell-car-privately-vs-trade-in.html`에 2문단짜리 "third-party buyer" 언급이 있었지만 CarMax/Carvana를 묶어서만 다뤘음 → 이번 글은 각 회사 프로세스를 개별적으로 깊게 비교(감정방식, 페이오프 처리속도 차이 등)해서 중복 아님.
  - `how-to-price-car-for-private-sale.html` (896단어) — 기존 가치평가 계산기(`used-car-value-calculator`)와 다른 각도(가격 전략/네고 여지), 실제 검증된 예시표 포함.
  - `how-to-sell-car-with-loan-still-on-it.html` (874단어) — 기존 글에 100단어짜리 "You still owe money" 시나리오박스가 있었지만 이번 글은 10일 페이오프 견적, 리엔 해제, 사설 매매 시 에스크로 처리 등 훨씬 깊게 다뤄서 중복 아님.
  - `how-to-avoid-scams-selling-car-privately.html` (917단어) — 기존 `how-to-buy-used-car-without-getting-ripped-off.html`은 "구매자가 당하는 사기"였고 이번 글은 "판매자가 당하는 사기"라 반대 관점, 중복 아님.
- **기존 2개 재분류(콘텐츠 변경 없음, 태그만 정정)**: `how-to-sell-car-privately-vs-trade-in.html`(Buying→Selling), `when-to-trade-in-your-car.html`(Ownership→Selling) — 새 카테고리가 첫날부터 6개 항목으로 시작하도록.
- **7/15 교훈 재적용**: 신규 4개 전부 색인된 페이지 3곳씩 링크 확보(스크립트로 재검증 완료) — `used-car-value-calculator`(4개 전부), `car-depreciation-calculator`(2개), `how-much-car-can-i-afford`(2개), `how-to-check-car-history-before-buying`(1개), 홈페이지 latest-3(3개).
- **사이트 전체 반영**: `blog/index.html`(Latest 섹션 최상단 갱신 + 신규 "🤝 Selling & Trade-In" 카테고리 섹션 신설, 기존 2개 카드는 원래 섹션에서 제거하고 이동), `index.html`(홈페이지 latest-3 전부 교체), `sitemap.xml`(81개 URL), `llms.txt`(신규 "Selling & Trade-In" 섹션 신설, 기존 2개 항목 이동).
- **검증**: 태그밸런스(div/a/ul/li)·JSON-LD 유효성·사이트 전체 깨진링크(0건)·sitemap XML 유효성·신규 4개 전부 색인페이지 링크 3개씩 확보 여부를 전부 스크립트로 확인 완료.
- 커밋 `226f6f9`, 14개 파일.
- **최종 결과**: 사이트는 이제 블로그 51개 + 툴 22개 = 73개 페이지, sitemap 81개 URL. 오늘 하루 총 신규 발행: 블로그 7개(cash-vs-finance, CPO, extended warranty, CarMax vs Carvana, 가격책정, 대출차량판매, 사기예방) + 툴 1개(cash-vs-finance-calculator) = 8개.
- **⚠️ 다음 세션 필독**:
  1. 오늘 신규 발행한 8개 전부(+재분류 2개) 색인 여부를 1~2주 후 확인 대상에 포함. 특히 "Selling & Trade-In" 카테고리 전체(6개)가 하나의 신호 세트로 묶여서 움직이는지(전부 색인되거나 전부 안 되거나) 관찰하면 "카테고리 단위로 신뢰도가 쌓이는지" 여부에 대한 힌트가 될 수 있음.
  2. 사용자가 "카테고리를 늘리는 게 색인에 도움될 것"이라는 가설을 갖고 있음 — 다음 세션에서 색인 데이터로 이 가설이 맞는지 실제로 검증할 것. 맞으면 카테고리 확장을 계속할 근거가 되고, 안 맞으면(콘텐츠 양보다 역시 링크/권위가 핵심이라면) 방향을 다시 사용자와 논의할 것.
  3. `blog/index.html`의 Latest 섹션이 이제 13개 항목으로 늘어남(원래 11개 안팎이었음) — 다음 세션에서 시각적으로 너무 길어 보이지 않는지 확인 권장. 카드 그리드라 무한정 늘어나도 레이아웃 자체는 깨지지 않지만, UX 관점에서 "Latest"를 최근 N개로 캡핑하는 정책을 도입할지 사용자와 논의해볼 만함.
  4. 다른 카테고리(신규 운전자, 차종별 가이드 등)도 사용자가 관심 보이면 같은 방식(경쟁강도 확인 → 기존 콘텐츠 재분류 가능 여부 확인 → 4개 내외로 시작)으로 확장 가능.

## 6-6. 7/17 세션(6차): "Glossary" 신설 — Tools/Blog와 나란한 3번째 최상위 섹션
- **배경**: 6-5에서 만든 게 Blog 하위 카테고리인 걸 사용자가 확인하면서 "Tool/Blog 외의 것"을 원한다는 게 명확해짐 — 헤더 내비게이션(Tools|Blog|About)에 새 항목이 생기는 수준의 진짜 3번째 섹션을 요청.
- **방향 결정**: Glossary(용어사전)/State Guides(주별 가이드)/Reviews(차량 리뷰) 3개 옵션을 장단점과 함께 제시 → Reviews는 Edmunds/KBB급 완전 독점 + 사이트 정체성과 안 맞아 배제 추천, State Guides는 정확도 리스크+경쟁 문제로 2순위, Glossary를 1순위로 추천하고 승인받음.
- **콘텐츠 설계 방향 수정**: 사용자가 "용어별로 낱개 페이지 만들면 또 저가치 콘텐츠 문제(7/13 AdSense 플래그 재발 우려)"를 정확히 짚음 → 용어 하나=페이지 하나 대신 **카테고리별로 묶어서 페이지당 여러 용어**로 설계 변경. 결과적으로 4페이지(재무/구매/소유가치/판매) 전부 800단어 이상 확보.
- **신규 구조**: `/glossary/` 폴더 신설 — `index.html`(카테고리 랜딩), `financing-terms.html`(13개 용어, 825단어), `buying-terms.html`(10개 용어, 805단어), `ownership-value-terms.html`(9개 용어, 823단어), `selling-terms.html`(8개 용어, 812단어). 각 용어는 사전적 한 줄 정의가 아니라 맥락 설명(1~3문장) + 관련 있으면 기존 전체 가이드/계산기로 링크 — 그냥 정의만 나열하는 대신 사이트 내 기존 콘텐츠로 트래픽을 분산시키는 허브 역할도 겸함.
- **사이트 구조 변경 (중요, 전체 페이지 영향)**:
  - `assets/partials/header.html`에 "Glossary" 내비게이션 항목 추가 (Tools/Blog/**Glossary**/About) — 공유 파샬이라 전체 사이트에 자동 반영됨.
  - `assets/partials/footer.html`에도 Glossary 링크 추가 — 이 덕분에 **glossary/index.html은 사이트의 모든 페이지(색인된 16개 포함)에서 자동으로 링크를 받음**, 별도 작업 불필요.
  - `assets/js/components.js`의 `isToolPage` 판별 로직에 `/glossary/` 제외 조건 추가 — 안 했으면 글로서리 페이지에 엉뚱하게 "← All tools" 백링크가 뜰 뻔했음(배포 전 직접 발견하고 수정, 실제 사이트에 반영 안 됨).
- **7/15 교훈 적용**: 카테고리 페이지 4개(index 제외, index는 푸터로 이미 충분) 전부 색인된 페이지로부터 링크 2개씩 확보 — `financing-terms`(car-loan-calculator, how-to-get-pre-approved-car-loan), `buying-terms`(how-to-negotiate-car-price-at-dealership, how-to-check-car-history-before-buying), `ownership-value-terms`(car-depreciation-calculator, how-much-car-can-i-afford), `selling-terms`(used-car-value-calculator, car-insurance-estimator).
- **검증**: 태그밸런스(div/a/ul/li)·JSON-LD 유효성·헤더/푸터 파샬·`components.js` 문법(node로 검증)·사이트 전체 깨진링크(0건)·sitemap XML 유효성 전부 스크립트로 확인 완료.
- sitemap.xml(+5 URL, 86개), llms.txt(신규 "Glossary" 섹션) 반영.
- 커밋 `a41d617`, 18개 파일.
- **최종 결과**: 사이트는 이제 Tools(22) + Blog(51) + **Glossary(4, 신규)** = 77페이지 + 정적페이지, sitemap 86개 URL. 헤더 내비게이션이 Tools\|Blog\|About 3개에서 Tools\|Blog\|**Glossary**\|About 4개로 늘어남 — **오늘 세션 중 유일하게 사이트 전체 헤더/푸터에 영향을 준 변경**이라 다음 세션에서 반드시 화면으로 확인할 것.
- **⚠️ 다음 세션 필독**:
  1. **최우선**: 헤더 내비게이션에 "Glossary"가 정상적으로 뜨는지, 모바일 햄버거 메뉴에서도 정상 작동하는지 화면으로 직접 확인. 오늘 세션 중 유일한 사이트 전체(헤더/푸터) 변경이라 다른 신규 페이지 확인보다 우선순위 높음.
  2. 용어사전 4개 페이지도 색인 여부 확인 대상에 포함(1~2주 후).
  3. 사이트에 이제 **3개의 신규/확장 축**이 동시에 진행 중: (a) 기존 미색인 50개 링크 보강(7/15), (b) Selling & Trade-In 블로그 카테고리(7/17 5차), (c) Glossary 섹션(7/17 6차). 다음 색인 데이터 확인할 때 이 세 가지를 각각 분리해서 어떤 게 효과 있었는지 비교해볼 것 — 한꺼번에 너무 많이 바뀌어서 "무엇 때문에 좋아졌는지" 헷갈릴 수 있으니 이 기록을 참고할 것.
  4. Glossary도 사용자가 "확장 원한다"고 하면 같은 패턴(카테고리 묶음, 800단어 이상, 관련 가이드로 링크)으로 용어 추가 가능 — 예: EV 관련 용어, 보험 관련 용어(단, 보험은 이미 "방치 정책" 영역이라 우선순위 낮음).
  5. **(7차 추가)** Glossary 4페이지에 기술적 보강 완료: 용어 40개 전체 h2에 anchor id 추가(딥링크 가능) + DefinedTermSet JSON-LD에 hasDefinedTerm 배열로 용어 40개 개별 구조화 데이터 추가. 개별 용어 키워드 경쟁강도는 체크 안 함(Investopedia/NerdWallet급이 이미 장악, 개별 용어로 순위 경쟁은 비효율 판단) — 이건 신규 트래픽용이 아니라 검색엔진/AI검색이 페이지를 더 잘 파싱하게 하는 기술적 보강. 커밋 `a1d224f`.

## 6-7. 7/19 세션: Quick answer 템플릿 확장 보강 + 신규 콘텐츠 2건(0% APR vs 리베이트, 리스 바이아웃)

- **⚠️ 첨부파일 미수신**: 사용자가 서치콘솔 스크린샷을 첨부했다고 언급했으나 실제로는 업로드되지 않음(uploads 폴더 빈 상태로 확인). AdSense 재검토 결과도 여전히 미확인(7/13 제출 이후 계속). 이번 세션은 handover 7/17 시점의 마지막 확인된 GSC 데이터를 기준으로 판단해서 진행 — **다음 세션 시작 시 실제 GSC 스크린샷/자료 재요청 필요, AdSense 상태도 재확인 필요**.
- **작업 우선순위 판단 기준**: 사용자가 "AI검색은 도메인 권위보다 콘텐츠 내용, 문제해결/비교분석이 유리"라고 명시적으로 언급 → (1) 이미 순위가 검증된 최상위 페이지들에 AI검색 대응 보강(Quick answer 콜아웃) 확장 적용, (2) 신규 롱테일 갭 발굴 두 트랙으로 진행.

### 트랙 1 — Quick answer 콜아웃 확장 적용 (5개 페이지, 신규 콘텐츠 아님)
7/17-1차 세션에서 만든 "Quick answer" 패턴(문제해결형 요약 박스, highlight-box 재사용)이 사이트 최상위 랭킹 페이지들엔 적용 안 돼 있던 것을 발견 — grep으로 전수 확인 후 다음 5개에 확장 적용. **전부 본문에 이미 있는 검증된 수치를 파이썬으로 재검증해서 그대로 인용**(신규 수치 추측 없음):
- `tools/car-loan-calculator.html` (사이트 1위, 4.07위)
- `tools/car-down-payment-calculator.html` (7.75위)
- `tools/road-trip-cost-calculator.html` (7.44위)
- `blog/how-to-check-car-history-before-buying.html` (9.6위)
- `blog/how-to-negotiate-car-price-at-dealership.html` (27.5위)

각각 dateModified(JSON-LD)와 sitemap lastmod 갱신, 태그밸런스 스크립트로 재검증 완료.

### 트랙 2 — 롱테일 키워드 리서치 (웹서치로 경쟁강도 확인, 기존 콘텐츠 전수 대조)
아래 5개 후보를 조사했고, 3개는 기각·2개는 채택:
- ❌ **"credit union vs bank car loan"**: 개별 신협·은행들이 각자 자체 발행하는 초포화 주제(Broadview FCU, Solarity CU, Focus FCU 등 전부 동일한 글 발행) — 승산 없음, 기각.
- ❌ **"차량 압류(repossession)"**: CFPB·FTC(정부)·Upsolve·Justia(법률구조단체)가 독점 + YMYL 리스크 높고 계산기 사이트 정체성과 안 맞음 — 기각.
- ❌ **"gap insurance is it worth it"**: 보험 카테고리(기존에 "의도적 방치" 결정된 영역과 동일 성격) — 기각.
- ❌ **"trade-in 세금 크레딧"**: `tools/car-sales-tax-calculator.html`에 이미 2,253단어로 충분히 다뤄짐 — 중복 확인, 기각.
- ✅ **"0% APR financing vs cash rebate"**: Edmunds가 자체 계산기를 갖고 있지만(진짜 경쟁자), realcartips.com·mortgagecalculator.org·carleases.org 같은 소형 사이트도 섞여 있어 승산 있음. 기존 사이트에 "현금 vs 대출"(`should-you-pay-cash-or-finance-a-car`), "리파이낸스"(`car-refinance-calculator`)는 있지만 "0% APR vs 리베이트" 자체를 다루는 콘텐츠는 없음 — 진짜 갭 확인.
- ✅ **"리스 만료 시 바이아웃 여부"**: leaseend.com(전용 계산기 보유한 소형 특화 사이트)이 섞여 있어 승산 있음. 기존 `should-i-buy-or-lease-a-car`(초기 리스 vs 구매 결정)·`how-to-get-out-of-a-car-lease-early`(조기 해지)와 겹치지 않는 "만료 시점 바이아웃 여부" 진짜 갭 확인.

### 신규 콘텐츠 3건 (전부 900단어 이상 기준 충족, 파이썬/node로 수치·문법 이중 검증)
- **`tools/zero-percent-apr-vs-rebate-calculator.html`** (871단어, 신규 툴): 0% APR 노선과 리베이트+시중금리 노선을 동시 amortize해서 비교. 두 노선 다 표준 상환공식 사용, JS 로직을 node로 별도 재계산해서 본문 수치와 일치 확인.
- **`blog/zero-percent-apr-vs-cash-rebate-which-is-better.html`** (1,062단어, 신규 블로그, Financing 태그): 위 툴의 짝 콘텐츠. Quick answer 콜아웃 + Two Worked Examples + 비교표. **작업 중 발견한 실수**: Example 2의 이자 수치를 처음에 "$2,001"로 잘못 기재했다가 파이썬 재검증 과정에서 실제값 "$4,001"과 다른 것을 발견해 즉시 수정함(규칙 7 재확인 사례 — 발행 전 전수 재계산 습관이 실제로 오류를 잡아낸 케이스).
- **`blog/should-you-buy-out-your-car-lease.html`** (955단어, 신규 블로그, Buying 태그): 리스 바이아웃 여부를 "잔존가치 vs 시장가치" 비교로 판단하는 가이드. 신규 전용 계산기는 만들지 않고 기존 `car-loan-calculator`(바이아웃 대출 시)·`used-car-value-calculator`(시장가치 확인)로 연결(CPO worth-it 글이 신규 계산기 없이 기존 `used-car-value-calculator`와 연결된 패턴과 동일).

### 사이트 전체 반영
- **내부링크(7/15 교훈 재적용)**: 신규 3개 전부 이미 색인된 페이지로부터 링크 확보. 단, `car-loan-calculator`(Related Guides 15개)·`used-car-value-calculator`(18개)·`how-much-car-can-i-afford`(16개)는 이미 리스트가 길다고 7/17 세션에서 지적된 페이지라 **의도적으로 제외**하고, 상대적으로 짧은 페이지 위주로 배분: `what-is-good-interest-rate-car-loan`(10→11)·`car-down-payment-calculator`(13→14) → 0% APR 툴 / `how-to-negotiate-car-price-at-dealership`(7→8)·`how-to-get-pre-approved-car-loan`(12→14) → 0% APR 블로그 / `car-depreciation-calculator`(13→14)·`how-to-check-car-history-before-buying`(7→8)·`how-to-get-pre-approved-car-loan` → 리스 바이아웃 블로그. 신규 3개 전부 인바운드 링크 4개 이상(홈페이지 포함) 확보 완료, 스크립트로 재확인.
- **`blog/index.html` Latest 섹션 정리**: 신규 2개 추가 전 확인해보니 Latest가 이미 19개 항목까지 늘어나 있었음(7/17 5차 세션 예상치인 13개보다 훨씬 많음 — 그 뒤 세션들에서 계속 추가되며 누적된 것으로 보임). 사용자 지시 없이 큰 구조 변경은 하지 않되, "Latest"가 실제로 최신 항목만 보여주는 취지에 맞게 **6월 게재분(Updated 배지) 4개를 Latest 하이라이트에서만 제외**(카테고리 섹션에는 그대로 유지, 삭제 아님)하고 신규 2개를 최상단에 추가 — 최종 15개. **이건 제 판단으로 진행한 가벼운 정리라 다음 세션에서 사용자 확인 권장** (7/17 5차 세션에서 이미 "너무 길어지면 캡핑 정책 논의" 필요성이 언급된 바 있음).
- `blog/index.html` Financing/Buying 카테고리 섹션에도 신규 2개 각각 최상단 추가.
- `tools/index.html` Financing 섹션에 신규 툴 추가.
- `index.html`: 툴 그리드에 신규 카드 추가, "22+"→"23+" 스탯 2곳(Free tools, Tools available) 갱신, 홈페이지 최신 블로그 3개 미리보기를 신규 2개 + 기존 최신 1개(CarMax vs Carvana)로 교체.
- `sitemap.xml`: 신규 3개 URL 추가(89개), 보강 5개 페이지 lastmod 갱신.
- `llms.txt`: 신규 3개 항목 각 카테고리에 추가.
- **검증**: 태그밸런스(div/p/h1-3/ul/li/table/tr/th/td) 전체 스크립트 확인, JSON-LD 유효성 전체 확인, 사이트 전체 818개 href 전수 스캔(실제 깨진 링크 0건 — {{BASE}} 템플릿 플레이스홀더 관련 false positive 11건만 있었고 이는 header/footer partial이 JS로 처리되는 정상 패턴), sitemap XML 유효성(89 URL) 확인, 신규 3개 전부 인바운드 링크 4개 이상 확인. 전부 스크립트로 재확인 완료.
- **최종 결과**: 블로그 51→53개, 툴 22→23개, sitemap 86→89 URL.
- **⚠️ 다음 세션 필독**:
  1. **최우선**: 실제 서치콘솔 자료 재요청, AdSense 재검토 결과 재확인 — 둘 다 이번 세션에서도 확인 못 함.
  2. 오늘 신규 발행한 3개(0% APR 툴/블로그, 리스 바이아웃 블로그) 색인 여부 1~2주 후 확인 대상 포함.
  3. `blog/index.html` Latest 섹션에서 뺀 6월 게재분 4개(`how-to-get-out-of-a-car-lease-early`, `what-happens-when-car-loan-is-paid-off`, `best-time-of-year-to-buy-a-car`, `what-credit-score-do-you-need-to-buy-a-car`) — 카테고리 섹션엔 남아있어 사이트에서 사라진 건 아니지만, 이 판단(Latest는 최근 N개로 캡핑)에 대해 사용자 확인 받을 것. 동의하면 이후 세션에도 이 방식(신규 추가 시 가장 오래된 것부터 정리) 유지, 반대하면 원복.
  4. 트랙 2에서 기각한 3개 주제(신협 vs 은행, 압류, 갭보험 worth-it)는 향후에도 재검토 불필요 — 각각 이유가 구조적(초포화/YMYL/보험 방치정책)이라 시간이 지나도 안 바뀔 가능성 높음.

## 6-8. 7/19 세션 후속: 실제 GSC export 확인 + `how-much-car-can-i-afford.html` Quick answer 보강

- 사용자가 깜빡했던 실제 서치콘솔 export(Coverage + Performance zip)를 뒤늦게 전달 — 압축 해제해서 전수 확인함. 상세 수치는 위 5번 섹션에 전부 반영 완료.
- **핵심 결론**: 6-7 세션(같은 날 앞서 진행)의 판단 방향은 이 실제 데이터와 어긋나지 않음. 다만 실제 노출 데이터로 재확인하는 과정에서 **`how-much-car-can-i-afford.html`이 노출 110회로 사이트 전체 1위이고, 그 안의 "rules of thumb 2026" 쿼리 클러스터가 2~6위까지 나오는 확인된 사이트 최고 성과 페이지인데도 6-7 세션에서 Quick answer 보강 대상 5개에서 빠졌던 것**을 발견 → 이번에 추가로 보강함.
- `blog/how-much-car-can-i-afford.html`: 인트로 문단 바로 뒤(첫 H2 앞)에 Quick answer 콜아웃 추가. 이미 본문에 있던 20/4/10 규칙 + "$5,000/월 소득 → $500/월 상한" 예시를 그대로 재사용(새 수치 추측 없음), 태그밸런스·JSON-LD 검증 완료, dateModified·sitemap lastmod 갱신.
- **⚠️ 다음 세션 필독 추가**: 이 페이지 보강 효과는 다음 GSC 확인(최소 7/22 이후, Coverage 리포트 지연 감안) 때 "rules of thumb" 클러스터 순위·노출이 유지/개선됐는지로 판단할 것. 참고로 이 페이지는 노출 표본이 이미 110회로 사이트에서 가장 크기 때문에, 다른 소표본 페이지들과 달리 이번엔 순위 변화가 있다면 통계적으로 의미 있게 읽어도 됨(rule 6과 별개 취급).

## 6-9. 7/21 세션: 연방 EV 세금혜택 오류 정정(최우선) + 신규 EV 리스vs구매 블로그 + 코사이너 클러스터(블로그+툴)

- **작업 트리거**: 사용자가 일요일 주간 루틴을 앞당겨 진행 지시. 첨부 자료(보고서 개요 CSV + Coverage/Performance zip, 2026-07-21 export)로 시작.
- **GSC 재확인**: Coverage는 여전히 7/10 데이터까지만 반영(1~2주 지연 계속), **색인 생성됨 16개가 6/6부터 지금까지 7주 이상 정체 그대로** — 7/15 내부링크 보강의 효과는 이번에도 판단 불가(데이터 컷오프가 그 이전). Performance도 지난 세션(7/19)과 사실상 동일한 패턴(클릭 0, "car affordability rules of thumb 2026" 클러스터 2~4위 유지, 노출 표본 대부분 여전히 작음) — 새로운 액션 시그널 없음.
- **⚠️ 중대 발견 (이번 세션 최우선 작업으로 전환)**: 사이트 내 EV 관련 페이지 3개가 **이미 종료된 연방 EV 세금혜택을 여전히 유효한 것처럼 서술 중**이었음.
  - 웹서치로 IRS.gov 등 다수 독립 출처 교차검증 결과: $7,500(신차)/$4,000(중고) 연방 EV 세금혜택(30D/25E)과 리스 시 활용되던 상업용 크레딧 루프홀(45W)이 **2025년 7월 4일 서명된 One Big Beautiful Bill Act(OBBBA)로 2025년 9월 30일부로 전부 종료**됨(구매/계약+결제를 9/30 이전에 마친 경우만 Form 8936으로 예외 청구 가능). 대체 성격으로 **자동차 대출 이자공제**(연 $10,000 한도, 미국산 신차 한정, 2025~2028년 한시, 소득에 따라 phase-out) 신설됨. **홈 EV충전기 세액공제(Section 30C, 30%/$1,000 한도)도 2026년 6월 30일 종료** — 오늘(7/21) 기준 이미 지난 상태.
  - `blog/ev-tax-credit-2026.html` **전면 재작성**: 혜택 종료 사실, 유일한 예외조항, 리스 루프홀 종료, 실제 남은 혜택(대출이자공제/홈충전기 상태/주별 인센티브/제조사 자체 인센티브) 정리. 1,401단어.
  - `tools/gas-vs-ev-savings-calculator.html`: "연방 세금혜택이 가격차를 좁혀준다"는 구절 수정, 현재 남은 혜택으로 대체.
  - `blog/electric-vs-gas-car-true-cost.html`: **5년 총비용 예시를 크레딧 제외하고 파이썬으로 재계산 — 결론이 "EV가 $1,400 저렴"에서 "가스차가 약 $6,100 저렴"로 뒤바뀜**(같은 조건, 20,000mi/yr 고주행에서도 가스차가 여전히 ~$3,165 저렴, 15,000mi/yr·8년 보유 시에만 격차 ~$800로 근접). "누가 EV로 이득 보는가" 리스트도 "연방 세금혜택 대상자" 항목 제거하고 현실적 기준으로 교체. 홈충전기 세액공제(Section 30C) 만료 사실도 반영.
  - 사이트 전체에서 "$7,500"/"federal ev tax credit"/"clean vehicle credit" 언급 전수 재확인 — 위 3개 파일 외에는 전부 무관한 문맥(보험료, 주행거리 할인 기준 등)으로 확인, 추가 수정 불필요.
- **신규 블로그 1건 — `blog/ev-lease-vs-buy-2026.html`** (1,381단어, EV 태그): 위 세금혜택 정정과 직접 연결되는 시의성 있는 진짜 갭(리스 루프홀 종료로 리스vs구매 계산법 자체가 바뀜). **경쟁강도 확인**: 웹서치 결과 US News/Experian/Consumer Reports/NerdWallet급 대형사이트와 함께 thechargeport.com 같은 소형 EV 전용 계산기 사이트도 상위권에 섞여 있어 승산 있다고 판단. 기존 `should-i-buy-or-lease-a-car.html`(일반 차량, EV 언급 전무 확인)과 겹치지 않는 EV 특화 콘텐츠. 구매측 수치는 파이썬 상환공식으로 검증, 리스측은 가상의 money factor/잔존율을 지어내는 대신 **Experian의 실제 발표 통계(리스가 평균 $88~175/월 저렴)**를 인용해 과장된 정밀도를 피함.
- **신규 클러스터 — 코사이너(공동서명)**: 사이트 전체 검색 결과 코사이너 관련 콘텐츠 전무 확인(진짜 갭). **경쟁강도 확인**: LendingTree/Bankrate 등 대형 매체와 함께 소형 계산기 사이트도 혼재해 승산 있다고 판단.
  - `tools/auto-loan-cosigner-calculator.html` (1,077단어): 솔로 APR vs 코사인 APR 상환 비교. 파이썬으로 사전 검증 후 JS 이식, node로 문법 검증.
  - `blog/do-you-need-a-cosigner-for-a-car-loan.html` (1,105단어, Financing 태그): 코사이너의 실제 절감액(예시 2건, 파이썬 검증) + 코사이너가 지는 실제 리스크(전액 법적 책임, 신용보고서 반영, 제거의 어려움) 균형 있게 서술.
- **기각한 후보 4건 (경쟁강도/적합성 문제로)**:
  - ❌ 신용 없는 첫차 구매자: BHPH 딜러·서브프라임 렌더 리드젠 사이트로 완전 포화, YMYL 성격도 있어 기존에 기각된 "신협 vs 은행"과 동일 구조 판단.
  - ❌ 코사이너 제거 방법: JD Power/Experian/LendingTree/Bankrate급 대형 금융매체가 완전 독점 — "권위도 문제로 콘텐츠로 해결 안 되는" 기존 판단 사례(`how-to-get-pre-approved-car-loan`)와 동일 패턴.
  - ❌ 신차 vs 중고차 총비용 비교: 웹서치 결과 ampauto.io/carcostbreakdown.com/wealthvieu.com/digitalcalculator.info 등 **우리와 동급인 소형 계산기 사이트들이 이미 여러 개 이 주제를 선점**해 과포화 — 신규 진입 실익 낮다고 판단.
  - ❌ EV 홈충전기 설치비용: 홈 임프루브먼트/전기공사 소형 사이트(usecalcpro.com, ibelectric.com 등)로 과포화 + 사이트 정체성(자동차 금융 계산기)과 결이 다른 주제라 배제.
- **내부링크(7/15 교훈 재적용)**: 신규 3개 페이지 전부 기존 페이지에서 링크 확보 — `should-i-buy-or-lease-a-car`·`how-to-negotiate-car-price-at-dealership`(EV 리스vs구매), `car-refinance-calculator`·`how-to-refinance-a-car-loan`(코사이너), 홈페이지 최신 3개 미리보기·툴 그리드(둘 다). 스크립트로 재확인한 인바운드 링크 수: `ev-lease-vs-buy-2026`(9), `do-you-need-a-cosigner`(5), `auto-loan-cosigner-calculator`(6), `ev-tax-credit-2026`(10, 정정 후 기존 링크 유지).
- **사이트 전체 반영**: `blog/index.html`(Latest + EV/Financing 카테고리 섹션), `tools/index.html`(Financing 섹션), `index.html`(latest-3, 툴 그리드, 스탯 "23+"→"24+" 2곳), `sitemap.xml`(+3 URL, 92개, 정정 3개+링크 추가 4개 파일 lastmod 갱신), `llms.txt`(신규 항목 추가, EV 세금혜택 설명 정정).
- **검증**: div/p/ul/li/a/table/tr/td/th 태그밸런스, JSON-LD 유효성, sitemap XML 유효성을 스크립트로 전체 재확인. **사이트 전체 .html 링크 전수 스캔 — 깨진 링크 0건** 확인.
- 커밋 `ea1a870`, 15개 파일 (신규 3 + 수정 12).
- **최종 결과**: 블로그 51→53개, 툴 23→24개, sitemap 89→92 URL.
- **⚠️ 다음 세션 필독**:
  1. **AdSense 재검토 결과 여전히 미확인** — 7/13 제출 이후 계속 확인 안 됨, 다음 세션 최우선으로 확인할 것.
  2. 색인 생성 수(16개, 7주 정체)가 이번에도 최신 데이터로 확인 안 됨 — Coverage 리포트 지연이 계속 1~2주라 다음다음 세션쯤 봐야 함. 7/15 내부링크 보강 효과 판단이 계속 미뤄지고 있다는 점 인지할 것.
  3. 오늘 신규 발행 3개(EV 리스vs구매, 코사이너 블로그·툴) + 전면 재작성 1개(ev-tax-credit-2026) 전부 색인 여부 확인 대상에 포함.
  4. **오늘 발견한 "이미 종료된 혜택을 유효한 것처럼 서술" 패턴은 EV 세금혜택에 국한되지 않을 수 있음** — 다음 세션에서 여유 있으면 다른 시효성 있는 법/제도 언급(예: 주별 세율, 신용점수 기준, 인플레이션 관련 수치)이 있는 페이지들도 최신성 재확인 가치 있음. AdSense 저가치 콘텐츠 플래그(7/13)의 재발을 막는 차원에서도 정확성 점검은 지속 우선순위로 둘 만함.
  5. EV 카테고리가 이제 4개(electric-vs-gas, ev-lease-vs-buy, how-much-does-ev-cost-to-charge, ev-tax-credit)로 늘어남 — Selling/Glossary처럼 별도 카테고리로 분리할 만큼 커졌는지는 아직 판단 보류.
  6. 코사이너 관련 후속 콘텐츠(코사이너 제거 방법 등)는 대형 금융매체 독점 확인됨 — 향후에도 재검토 불필요, 구조적 이유(권위도 격차)라 시간 지나도 안 바뀔 가능성 높음.


- ~~FAQPage/HowTo 구조화 데이터~~ — **2026-05-07 Google이 FAQ 리치 리절트 완전 폐지 확인, 후보에서 제외됨** (7/12 3차 세션에서 정정)
- 통계치 들어가는 나머지 페이지(유지비 외 다른 페이지들)의 출처 표기 추가 확대 여지는 남아있음 — 이번엔 최고 트래픽 페이지 1개 + 감가상각 계산기만 처리

negative-equity/LTV/bi-weekly 클러스터(7/6·7/10 게시)의 색인·노출 여부 1~2주 후 재확인 필요
- 색인 생성 수가 7/6~7/10 보강분 이후 실제로 늘었는지 Coverage 리포트로 확인 (지연 감안, 최소 2주 후)
- `how-to-get-pre-approved-car-loan.html`처럼 "콘텐츠는 완벽한데 권위도 때문에 순위 안 나오는" 페이지들은 콘텐츠 작업 대신 **백링크/외부 채널 확대**가 근본 해법일 가능성 — 아직 미착수 영역 (단, 7/12 세션에서 "백링크는 이미 어느정도 있다"는 피드백 있었음, 우선순위 아님)

## 6-10. 7/22 세션: 광범위 키워드 리서치(3라운드) → 신규 클러스터 4개 + 신규 카테고리 1개 + 보강 1개 발행

- **작업 트리거**: 사용자가 "오늘은 신규를 좀 해볼까" 하며 순수 리서치부터 시작 지시. "바로 작업하지 말고 정리만" → 이후 세 차례에 걸쳐 "더 깊게 파봐", "클러스터끼리 연결해서 찾아봐", "신규 카테고리에서 또 파생 없는지" 요청받아 총 3라운드 리서치 진행 후 승인받고 실행.
- **리서치 방법론**: 1라운드(광범위 키워드 브레인스토밍+경쟁강도 확인) → 2라운드(1라운드에서 찾은 것들의 파생/유사 롱테일 재탐색 + 기각 항목 재검토) → 3라운드(신규 클러스터끼리 교차 조합 + 신규 카테고리 자체 확장 가능성 탐색). 총 20개 이상의 후보 키워드를 웹서치로 실제 경쟁사 문서수/퀄리티 확인 후 최종 4개 클러스터로 압축.
- **최종 승인된 신규 클러스터 4개 + 보강 1개**를 이번 세션에 전부 발행 완료 (수치 검증 → 작성 → 사이트 반영 → 검증 → 커밋/푸시까지 원샷 진행, 사용자가 "애드센스 심사 중이니 퀄리티 있게" 명시적으로 강조함).

### 신규 클러스터 1 — 카 서브스크립션 vs 리스 vs 구매
- `tools/car-subscription-vs-lease-vs-buy-calculator.html` + `blog/is-a-car-subscription-worth-it.html`
- 3자 실비용(보험+유지비 포함) 비교 계산기. 리스/서브스크립션 쪽은 가상의 money factor를 지어내는 대신 **실제 입력값(직접 견적 입력) 방식** 유지(기존 `car-lease-vs-buy-calculator.html`와 동일 컨벤션).
- **파이썬 검증 중 발견한 중요한 점**: 36개월 기준 예시 수치를 돌려보니 "구매가 장기적으로 항상 저렴하다"는 통념과 달리 **보조금 낀 리스가 구매보다 저렴하게 나옴**(리스는 감가상각분만 파이낸싱하기 때문) — 처음 작성했던 "퀵앤서"와 "예시 문단"이 이 계산 결과와 모순되길래 **과장 주장을 걷어내고 계산기 실제 출력과 일치하도록 카피 전면 수정**함. (품질 관리 차원에서 중요한 케이스로 기록)

### 신규 클러스터 2 — 2026 관세 영향 계산기
- `tools/car-tariff-impact-calculator.html` + `blog/how-do-tariffs-affect-your-car-payment-2026.html`
- VIN 첫 글자(국제 ISO 3779 WMI 표준) → 조립국 판정 → 국가별 관세 영향 추정치(Cox Automotive/AEG/JPMorgan 2026 리포트 출처) → 대출 상환액 재계산.
- **리서치로 확인된 사실**: "지금 사야 하나" 식 일반론은 KBB/Experian/CarEdge/AAA/딜러블로그로 완전 포화 — 반드시 "내 VIN + 내 대출액 기준 계산"이라는 좁은 각도만 유지해야 승산 있음(3라운드 교차탐색에서도 이 결론 재확인됨).
- **강한 디스클레이머 포함**: 국가별 수치는 전국 평균 추정치일 뿐 개별 차량 정확한 수치 아님, USMCA 재검토 진행 중이라 캐나다/멕시코 조립 차량 수치는 특히 변동 가능성 명시.

### 신규 클러스터 3 — 라이드셰어/긱워커 (신규 카테고리 "🚕 Gig & Rideshare" 신설)
- `tools/rideshare-car-cost-per-mile-calculator.html` + `blog/should-you-buy-a-car-for-uber-lyft-2026.html`
- **신규 카테고리를 만든 이유**: 3라운드 교차탐색 결과 이 클러스터만 유일하게 "개인 소비자"가 아닌 "소득창출용 차량 구매자"라는 완전히 다른 오디언스를 대상으로 함 — blog/index.html과 tools/index.html 양쪽에 "🚕 Gig & Rideshare" 카테고리 신설.
- buy/rent/lease 3자 비교, **리스 마일리지 초과료를 명시적으로 반영**(연 1만~1.2만 마일 캡 vs 풀타임 드라이버 실제 주행거리 3.5만~4.5만 마일 — 초과료 포함하면 리스가 가장 비싸짐, 파이썬+node로 재검증: buy $0.30/mi, rent $0.43/mi, lease $0.445/mi).
- **저경쟁 앵글로 확인된 부분**: 오토론 약관의 "영업용 사용 금지" 조항 — 우버/리프트로 돈 벌다가 대출 계약 위반이 될 수 있다는 파이낸싱 리스크는 검색 결과 autoloanrate.com/finhy.com 단 2곳만 다루고, 나머지는 전부 "보험" 얘기만 함. 이 각도를 블로그 핵심 섹션으로 반영.
- **신규 카테고리 자체 확장 시도는 전부 기각**: Turo 호스팅(수익화)은 Turo 공식 계산기+ROI 전용툴(rentscout.io)까지 있어 포화, Section 179 사업용 차량 세금공제는 section179.org(원출처, 자체 계산기 보유)가 이미 장악 — "Gig & Rideshare"는 이번 1세트로 시작, 무리한 확장 자제.

### 신규 클러스터 4 — 부부 공동명의(Joint) 오토론 vs 코사이너
- `blog/joint-auto-loan-vs-cosigner.html` — 7/21 세션에서 만든 코사이너 클러스터의 자연스러운 후속 확장.
- 이혼 시 조인트론 제거 관련 파생은 이번에 재확인 결과 RateGenius(2건)/RefiJet/CarsDirect/로펌 등으로 포화 확인 — 별도 페이지 대신 본문 내 짧은 리스크 섹션으로만 처리.

### 보강 1건 — 신규 자동차 대출 이자공제($10,000, OBBBA, 2025-2028) 반영
- 단독 신규 페이지는 기각(TurboTax/H&R Block/Jackson Hewitt/TaxAct + 니치 계산기 2개까지 이미 포화 확인) — 대신 **기존 3개 페이지에 단락 추가**: `tools/car-loan-calculator.html`, `blog/should-you-pay-cash-or-finance-a-car.html`, `blog/how-much-car-can-i-afford.html`.

### 이번 세션에서 리서치 후 최종 기각한 항목 (총 20개 이상, 사유는 커밋 메시지와 이전 대화 로그 참고)
84개월 대출(기존 72개월 글 자기잠식 우려), EV배터리 교체비용(10개+ 페이지 포화), 개인대출vs오토론(니치 계산기까지 존재), HELOC vs오토론, 하이브리드vsPHEVvsEV(Recharged 독점), 관세→중고차리플이펙트, 긱워커 마일리지세금공제(8개+ 포화), 서브스크립션 리스팅형, 주별판매세없는곳(기존 툴에 이미 있음), Repair vs Replace(계산기까지 이미 존재), 차색깔리세일, 가족증여/타이틀이전, 온라인구매(Carvana 특정브랜드), 관세×EV배터리광물(정책저널리즘 장르 불일치), EV트레이드인(Recharged 2건 선점), 이혼+조인트론제거(RateGenius 등 포화), Turo호스팅수익(공식계산기 존재), Section179사업용차량공제(원출처 사이트 장악), Turo vs Zipcar단기렌탈(장르 불일치).

### 사이트 전체 반영 내역
- `blog/index.html`: 신규 카테고리 "Gig & Rideshare" 섹션 신설, Buying/Financing 카테고리에 신규 4건 추가, Latest 섹션 최상단 갱신(현재 21개 항목 — 다음 세션에서 정리 검토 여지 있음, 7/19 세션에서 논의된 "오래된 것부터 트리밍" 방식 적용 안 함, 이번엔 그대로 둠).
- `tools/index.html`: 신규 카테고리 "Gig & Rideshare" 섹션 신설(라이드셰어 계산기), Financing 카테고리에 관세/서브스크립션 계산기 추가.
- `index.html`: 홈페이지 최신 블로그 미리보기 3개 전면 교체, 툴 그리드 카드 3개 추가, 스탯 카운터 "24+"→"27+" 2곳.
- `sitemap.xml`: 신규 URL 7개 추가(99개), 보강 3개 + 링크 추가 7개 = 총 10개 파일 lastmod 갱신.
- `llms.txt`: Tools/Buying/Financing 섹션에 신규 항목 추가, 신규 "Guides: Gig & Rideshare" 섹션 신설.
- **내부링크(7/15 교훈 재적용)**: 7개 기존 페이지(best-time-of-year-to-buy-a-car, car-lease-vs-buy-calculator, car-affordability-calculator, car-refinance-calculator 등)에서 신규 콘텐츠로 링크 추가. 스크립트로 재확인한 인바운드 링크 수: joint-auto-loan-vs-cosigner(3), car-subscription-vs-lease-vs-buy-calculator(6), is-a-car-subscription-worth-it(4), car-tariff-impact-calculator(4), how-do-tariffs-affect-your-car-payment-2026(5), rideshare-car-cost-per-mile-calculator(5), should-you-buy-a-car-for-uber-lyft-2026(4).

### 검증
- 전체 신규/변경 파일: div/p/ul/li/a/table/tr/td/th/select/option 태그밸런스, JSON-LD 유효성 스크립트로 확인.
- 신규 계산기 3개: JS 문법 node -c로 검증 + 파이썬/node로 실제 로직 재실행하여 카피 문구와 계산 결과 일치 재확인(특히 서브스크립션 계산기는 카피 수정까지 발생).
- sitemap.xml 유효성(99 URL), 사이트 전체 .html 링크 전수 스캔(깨진 링크 0건) 확인.
- 커밋 `7e04dd0`, 19개 파일 (신규 7 + 수정 12).
- **최종 결과**: 블로그 55→59개, 툴 24→27개, sitemap 92→99 URL, 카테고리 6→7개(Gig & Rideshare 신설).

### ⚠️ 다음 세션 필독
1. **AdSense 재검토 결과 여전히 미확인** — 7/13 제출 이후 계속 확인 안 됨, 다음 세션 최우선.
2. 오늘 신규 발행 7개 + 보강 3개 + 링크만 추가한 7개, 총 17개 파일의 색인 여부를 향후 GSC 확인 시 포함해서 볼 것.
3. blog/index.html Latest 섹션이 21개 항목으로 길어짐 — 트리밍 여부 사용자 확인 필요(7/19 세션에서 한 번 제안했다가 보류된 사안, 이번엔 손 안 댐).
4. **신규 카테고리 "Gig & Rideshare"는 현재 1세트(블로그+툴)만 있음** — 이 카테고리 확장 시도(Turo 호스팅, Section 179)는 이번에 전부 포화로 기각했으니 향후에도 무리하게 확장하지 말 것. 다만 완전히 새로운 긱워커 앵글(예: 다른 배달앱, 새로운 플랫폼 인센티브 변화)이 생기면 재검토 가치는 있음.
5. 관세 계산기의 국가별 추정 범위는 2026년 7월 시점 리서치 기준 — 특히 USMCA 재검토가 진행 중이라 캐나다/멕시코 조립 차량 관련 수치는 몇 달 내 실제로 바뀔 수 있음, 분기별로 재확인 권장.
6. 서브스크립션 계산기의 "quick answer" 카피는 이번에 실제 계산 결과에 맞춰 신중하게 수정함 — 향후 계산기 기본값(디폴트 입력값)을 바꾸는 경우, 카피에 있는 워크드 이그잼플 수치도 반드시 재검증할 것(이번처럼 계산기 출력과 카피 문구가 모순되지 않도록).
7. **7/22 세션 후속: UI 정렬 버그 수정** — 사용자가 스크린샷으로 `rideshare-car-cost-per-mile-calculator.html`의 "Your Driving Profile" 공유입력 행(4컬럼)이 데스크톱/모바일 둘 다 라벨 줄바꿈 길이가 달라 인풋박스가 삐뚤어져 보인다고 지적. 원인: 각 필드가 독립된 flex column이라 라벨이 1줄/2줄로 다르게 wrap되면 같은 행의 인풋 시작 높이가 달라짐. `.shared-grid label`에 `min-height`(2줄 분량)+`align-items:flex-end`로 라벨 높이를 통일해서 수정. **같은 패턴이 `car-subscription-vs-lease-vs-buy-calculator.html`의 "Shared Costs" 3컬럼 행에도 있어서 동일하게 수정**(`.shared-costs-row` 클래스 추가). 이번에 만든 계산기 3개 전체 재검사 결과 이 두 곳 외에는 동일 패턴 없음(다른 계산기들은 카드가 독립적으로 세로 스택되는 구조라 이 문제 자체가 발생 안 함). **다음에 "여러 필드가 한 행을 공유하는" 새 계산기 UI를 만들 때는 라벨 길이 편차를 미리 고려해서 이 min-height 패턴을 처음부터 적용할 것.** 커밋 `1148230`.


- 25개 사이트 등록 완료, footer 뱃지 6개 (NewTool, FoundrList, Fazier, Findly.tools, twelve.tools, PitchWall)
- **사용자가 총 11개 사이트를 운영 중** (autocalchub 포함). 필요시 본인 소유 다른 사이트에서 autocalchub로 상호링크 가능 — 7/15 세션에서 언급됨, **아직 착수 안 함, 지금 우선순위 아니라고 사용자가 명시적으로 보류함**. 다음에 백링크 관련 작업할 때 이 옵션 먼저 검토할 것. 단, 진행 시 유의점: (1) 상호링크가 명백히 기계적/전면적이면 Google 링크 스킴으로 인식될 리스크 있음 — 문맥상 자연스러운 곳에만 소량으로. (2) 나머지 10개 사이트가 뭔지, 주제가 얼마나 관련 있는지 다음 세션에서 먼저 파악 필요(사용자에게 목록 요청).

## 6-11. 7/27 세션 (일요일 주간 루틴 앞당김): EV 등록세 신규글+보강, 리스 테이크오버 신규 블로그+계산기

- **⚠️ 첨부파일 미수신**: 사용자가 서치콘솔+애널리틱스 자료를 첨부했다고 언급했으나 uploads 폴더 확인 결과 실제로는 업로드되지 않음 (7/19 세션과 동일 패턴, 이번이 두 번째). AdSense 재검토 결과도 여전히 미확인(7/13 제출 이후 계속). 이번 세션은 handover 7/21~7/22 시점의 마지막 확인된 GSC 데이터를 기준으로 판단해서 진행 — **다음 세션 시작 시 실제 GSC 자료 재요청 필요, AdSense 상태도 계속 재확인 필요**.
- **작업 우선순위 판단 기준**: 사용자가 "AI검색은 도메인 권위보다 콘텐츠 내용, 문제해결/비교분석이 유리"라고 재차 강조 + 애드센스 수익화(트래픽/클릭) 관점 우선순위 지시 → 리서치로 확인한 진짜 갭 위주로 문제해결/비교분석 구조 콘텐츠 작성.

### 리서치 (총 8개 후보 웹서치로 경쟁강도 확인, 6개 기각·2개 채택)
- ❌ **차량수당(Car Allowance) vs 마일리지 상환**: MileIQ/CompanyMileage/mBurse/Cardata/Timeero/TripLog 등 B2B 마일리지 추적 SaaS 업체들이 완전 장악 + 오디언스도 "개인 차량 구매자"가 아닌 "회사 정책 설계자" 위주라 사이트 성격과 불일치 — 기각.
- ❌ **리파이낸싱 없이 페이먼트 낮추기**: Bankrate/LendingTree/Experian/Kiplinger/Yahoo Finance급 대형 금융매체가 상위 완전 독점 — 기각.
- ❌ **벌룬페이먼트 자동차 대출**: SoFi/LendingTree/Motley Fool(fool.com)/Car and Driver 등 대형 사이트 위주 — 기각.
- ❌ **긱워커 1099 소득 대출승인**: Miramar Car Center/Dallas Lease Returns/Credit Acceptance/Auto Hive Direct 등 서브프라임 딜러 리드젠 사이트로 완전 포화(기존 "BHPH/신협vs은행" 기각 사례와 동일 구조) — 기각.
- ❌ **오토론 조기상환 페널티**: `tools/car-early-payoff-calculator.html`과 `blog/how-does-car-loan-interest-work.html`(Rule of 78s/precomputed interest 섹션)에 이미 충분히 다뤄짐 확인 — 중복, 기각.
- ❌ **리빌트/살비지 타이틀 파이낸싱**: `blog/is-it-worth-buying-car-with-rebuilt-title.html`에 "Financing a Rebuilt Title" 섹션으로 이미 다뤄짐 확인 — 중복, 기각.
- ✅ **EV 주별 등록세**: freedomforallamericans.org/SlashGear/costtocharge.com(소형 EV 계산기 사이트)/vehicletaxcalculator.com 등 소형 사이트 위주 + 정부 1차 출처(afdc.energy.gov) 혼재, NerdWallet급 대형매체 없음 — 채택. 사이트 내 기존 EV 콘텐츠 4건(electric-vs-gas/ev-lease-vs-buy/ev-charging/ev-tax-credit) 전수 확인 결과 등록세 언급 전무 — 진짜 갭 확인.
- ✅ **리스 테이크오버(취득자 관점)**: eautolease.com/capitalmotorcars.com/rusnakcars.com/drivespitzercdjr.com 등 개별 딜러 블로그 + lexingtonlaw.com 위주, 대형 금융매체 없음 — 채택. 기존 `how-to-get-out-of-a-car-lease-early.html`은 "양도자(세입자가 나가고 싶은 경우)" 관점만 다루고 "취득자(남의 리스를 넘겨받는 게 유리한지)" 관점은 전무 확인 — 차별화된 진짜 갭.

### 신규 블로그 1 — EV 주별 등록세
- `blog/ev-registration-fees-by-state-2026.html` (EV 태그, 약 950단어)
- 41개 주가 EV에 추가 연간 등록세 부과(전국 중앙값 $150/년), 미시간 $267~367/년으로 확인된 최고 수준, 펜실베이니아/텍사스 등 주별 표
- PHEV 차등부과(미시간 기준 EV의 절반 수준), 텍사스/뉴저지 등 일부 주는 신규등록 시 2~4년치를 한 번에 선납 청구하는 구조 등 문제해결형 콘텐츠로 구성
- Related Guides로 electric-vs-gas-car-true-cost/ev-tax-credit-2026/TCO계산기/gas-vs-ev계산기 연결

### 신규 블로그 2 — 리스 테이크오버(취득자 관점)
- `blog/is-a-lease-takeover-a-good-deal.html` (Buying 태그, 약 1,050단어)
- 총비용 비교 프레임 제시: (이관수수료 + 잔여 개월수×페이먼트) vs (신규리스 취득수수료+계약금+동일기간 페이먼트) — 월 페이먼트만 비교하는 흔한 실수를 지적하는 구조
- 주행거리 잔여량/마모 상태 점검, 리스사별 이관 허용 여부(기존 `how-to-get-out-of-a-car-lease-early.html`에 이미 검증된 수치 그대로 재사용: 토요타/혼다/BMW는 $300~500 수수료로 허용, VW 등은 불허), 책임 해제 조건 등 실전 체크리스트 포함

### 신규 툴 — 리스 테이크오버 비용 계산기
- `tools/lease-takeover-cost-calculator.html`
- 테이크오버 총비용(이관수수료+잔여 페이먼트-인센티브) vs 신규리스 총비용(취득수수료+계약금+동일기간 페이먼트) 비교, 복잡한 amortization 없이 단순 곱셈/덧셈 구조라 계산 오류 리스크 최소화
- 파이썬 + node 목업 DOM으로 계산 로직 이중 검증(기본값: 테이크오버 $5,440 vs 신규리스 $7,955, 차이 $2,515로 일치 확인)

### 보강 — EV 등록세 반영한 총비용 재계산
- `blog/electric-vs-gas-car-true-cost.html`: 5년 총비용 표에 등록세 항목이 누락돼 있던 것을 발견(기존 표는 구매가/연료비/유지비/보험료만 반영, 등록비 자체가 없었음). 파이썬으로 재계산해 반영: 5년 격차 $6,100→**$6,850**, 20,000마일/년 시나리오 $3,165→**$3,915**, 8년/15,000마일 시나리오 $800→**$1,550**. 신규 등록세 글로 연결하는 문단 추가.
- `tools/car-total-cost-of-ownership-calculator.html`: 등록세 설명 문단에 EV 서차지 관련 문장 추가, 신규 글로 연결.
- **품질 관리 참고**: 이번에도 7/22 세션(서브스크립션 계산기 카피 모순 발견)과 같은 유형의 이슈 — 기존 콘텐츠의 총비용 계산에 누락된 항목이 있는지 재검토하는 습관이 실제로 부정확한 격차 수치를 잡아낸 사례. 다른 EV 관련 페이지들의 총비용 계산도 유사한 누락이 없는지 여유 있을 때 재점검 가치 있음.

### 사이트 전체 반영 내역
- `blog/index.html`: Latest 섹션 최상단에 신규 2개 추가(21→23개 — **트리밍 미적용, 이번에도 손 안 댐**, 계속 늘어나는 중이라 다음 세션에서 캡핑 여부 사용자 확인 필요), Buying/EV 카테고리 섹션에 각각 추가.
- `tools/index.html`: Buying & Financing 섹션에 리스 테이크오버 계산기 카드 추가.
- `index.html`: 최신 블로그 미리보기 3개를 신규 2개 + 기존 최신 1개(should-you-buy-a-car-for-uber-lyft-2026)로 교체, 툴 그리드에 리스 테이크오버 계산기 카드 추가, 스탯 카운터 "27+"→"28+" 2곳(Free tools, Tools available).
- `sitemap.xml`: 신규 URL 3개 추가(99→102), 보강/링크추가 11개 파일(electric-vs-gas-car-true-cost, car-total-cost-of-ownership-calculator, gas-vs-ev-savings-calculator, ev-tax-credit-2026, how-much-does-ev-cost-to-charge-at-home, should-i-buy-or-lease-a-car, car-lease-vs-buy-calculator, how-to-get-out-of-a-car-lease-early, should-you-buy-out-your-car-lease, blog/, tools/, 홈페이지) lastmod 갱신.
- `llms.txt`: Tools 목록에 리스 테이크오버 계산기, EV 가이드 섹션에 등록세 글, Buying 가이드 섹션에 리스 테이크오버 글 추가.
- **내부링크(7/15 교훈 재적용)**: EV 관련 기존 페이지 3곳(ev-tax-credit-2026, gas-vs-ev-savings-calculator, how-much-does-ev-cost-to-charge-at-home), 리스 관련 기존 페이지 4곳(should-i-buy-or-lease-a-car, how-to-get-out-of-a-car-lease-early, should-you-buy-out-your-car-lease, car-lease-vs-buy-calculator)에서 신규 페이지로 링크 추가. 스크립트로 재확인한 인바운드 링크 수: `ev-registration-fees-by-state-2026`(7), `is-a-lease-takeover-a-good-deal`(6), `lease-takeover-cost-calculator`(4).

### 검증
- 신규/변경 파일 15개 전체: div/p/ul/li/a/table/tr/td/th/select/option/h1/h2/h3 태그밸런스 스크립트 확인, JSON-LD 유효성 확인 — 전부 통과.
- sitemap.xml 유효성(102 URL) 확인.
- 사이트 전체 .html 링크 844개 전수 스캔 — 깨진 링크 0건.
- 신규 계산기 JS: node -c 문법 검증 + 목업 DOM으로 실제 로직 실행, 파이썬 계산 결과와 일치 재확인(규칙 7 그대로 적용).
- 커밋 `9bad0b1`, 17개 파일 (신규 3 + 수정 14).
- **최종 결과**: 블로그 59→61개, 툴 27→28개, sitemap 99→102 URL.

### ⚠️ 다음 세션 필독
1. ~~실제 서치콘솔/애널리틱스 자료 재요청 필요~~ — **세션 후반부에 실제 자료 수신 및 분석 완료**(Coverage+Performance zip, GA4 개요 CSV). 상세 내용은 위 5번 섹션에 전부 반영. 핵심: 3개월 누적 첫 클릭 1건 발생(7/25, 홈페이지), 그 외 전부 정체. GA4 트래픽 상당수가 디렉토리 크롤러/본인 테스트 성격일 가능성 높다는 점 확인 — 향후 GA 해석 시 감안할 것.
2. **AdSense 재검토 결과 여전히 미확인** — 7/13 제출 이후 계속 확인 안 됨, 다음 세션 최우선.
3. 오늘 신규 발행 3개(EV 등록세 블로그, 리스 테이크오버 블로그+계산기) + 보강 2개(electric-vs-gas-car-true-cost, TCO계산기)의 색인 여부 향후 GSC 확인 시 포함해서 볼 것.
4. blog/index.html Latest 섹션이 이제 23개 항목 — 계속 늘어나는 중, 트리밍(캡핑) 정책 여부 사용자 확인 필요(7/19에 제안했다 보류, 이후 세션들에서도 계속 미루는 중).
5. 이번에 기각한 6개 주제(차량수당vs마일리지, 리파이낸싱없이 페이먼트낮추기, 벌룬페이먼트, 긱워커1099대출승인, 조기상환페널티, 리빌트타이틀파이낸싱)는 향후에도 재검토 불필요 — 각각 구조적 이유(SaaS경쟁/대형매체포화/중복콘텐츠)라 시간 지나도 안 바뀔 가능성 높음.
6. **다른 EV 페이지들도 총비용 계산에 등록세 외 누락된 비용 항목이 없는지 여유 있을 때 재점검 가치 있음** — 이번에 electric-vs-gas-car-true-cost.html에서 실제로 누락을 발견한 사례가 있어서, 유사 패턴이 다른 총비용 비교 콘텐츠에도 있을 수 있음.
7. EV 등록세는 주별로 매 회기 변경되는 항목 — 다음에 이 글 재검토할 때는 반기~1년 주기로 각 주 DMV 최신 수치 재확인 권장(관세 계산기와 유사한 시효성 이슈).


## 6-12. 8/7 세션: GSC/GA 분석 결과 콘텐츠 발행은 보류 + 수익화 정책 확정 + 제휴 대비 정책 문구 선제 수정

- **⚠️ 8/7 세션 중 사용자가 "발행 감속/중단" 제안을 명시적으로 기각함 — "그 고집을 버려라, 공격적 확장에는 변함이 없다".** 아래 색인 관련 분석(색인 21%, 미색인 격차 확대)은 여전히 유효한 사실 관찰이지만, **거기서 도출한 "발행 속도를 늦추자"는 정책 제안은 사용자가 거부함. 다음 세션부터 발행 속도를 줄이자고 다시 제안하지 말 것 — 공격적 확장 기조를 기본값으로 유지.** 색인 지연 자체는 계속 모니터링하되, 대응은 발행 감속이 아니라 다른 수단(백링크 등)으로 할 것.
- 이번 세션 자체는 GSC/GA 데이터상 새로 발행할 신규 콘텐츠 후보가 확정되지 않아 신규 발행 없이 종료(리서치한 오토 리파이낸스 프리퀄 영역은 대출기관 직접 장악으로 기각 — 이건 유효한 개별 판단, 확장 속도 문제와는 별개).
- **이전 세션 기록 정정**: 7/27 세션에서 "🎉 첫 클릭 발생"이라고 기록한 건 과대 해석이었음. 국가별로 뜯어보니 한국 노출 12회/클릭 1회/순위 1.17위 = 브랜드 직접 검색(본인 확인용)일 가능성이 압도적이고, 미국은 1,632회 노출에 클릭 0. **실질 오가닉 클릭은 여전히 0건.** 앞으로 클릭 지표는 반드시 국가·순위와 같이 볼 것.
- **수익화 정책 확정** — 사용자 지시로 섹션 5-1 신설(애드센스 비의존, 제휴 전방위 검토, 재심사·가입·철수는 Opus가 실익 판단, 애드센스보다 나은 대안이면 추천).
- **제휴 대비 정책 문구 선제 수정 완료(커밋 `30355b3`)** — 사용자가 "왜 지금 안 하냐"고 지적, 즉시 처리:
  - `editorial-policy.html`: "제휴 마케팅 안 함" 단정 문구 제거 → "How AutoCalcHub Makes Money"로 통합해 디스플레이 광고+제휴/리퍼럴 둘 다 포괄, FTC 공시 기준 언급. "Affiliate Disclosure" 섹션 신설(현재는 제휴링크 없지만 추가 시 링크 옆 개별 고지 원칙 + 파트너 선정 기준 명문화).
  - `privacy-policy.html`: "Advertising"→"Advertising & Affiliate Links"로 확장, 제휴 트래킹 쿠키 조항 추가.
  - sitemap.xml lastmod 갱신.
  - **교훈**: 지금 당장 할 수 있는 무료 작업(정책 문구 정리)을 "나중에 하겠다"고 미루면 안 됨 — 다음 세션에서 같은 판단 반복하지 말고, 실행 가능한 건 그 자리에서 바로 처리할 것.
- 사용자가 8/6에 직접 커밋(`9e2a3ca`)으로 `index.html`에 boostdomainrating 배지 추가 — 백링크 작업을 사용자가 병행 중.
- **다음 세션 확인 사항**: (1) 색인 수가 19개에서 더 올라갔는지, (2) 7/27 발행분 3개(EV 등록세, 리스 테이크오버 블로그+계산기)의 색인 여부, (3) 애드센스 재심사 결과 확인 여부, (4) 실제 제휴 프로그램 가입 시점 판단(트래픽 임계치 도달 여부).

## 6-13. 8/11 세션 (일요일 주간 루틴 앞당김): 오토론 이자공제(OBBBA) 클러스터 신규 4건

- **⚠️ 첨부파일 또 미수신 (3번째)**: 사용자가 서치콘솔+애널리틱스 자료를 첨부했다고 언급했으나 `/mnt/user-data/uploads` 확인 결과 비어 있음(7/19, 7/27에 이어 세 번째 동일 패턴). **"색인은 내가 준 걸로만 판단하면 된다"는 지시에 따라 5번 섹션의 8/7자 GSC 데이터를 기준으로 판단하고 진행함.** 다음 세션에서도 첨부 여부를 먼저 확인하고, 없으면 즉시 사용자에게 알린 뒤 마지막 확인 데이터로 진행할 것.
- **지시 사항**: 공격적 확장 기조 유지(변경 금지), 수익화 관점 우선순위, 롱테일 전략, 경쟁 회피 장치, 대시보드/시각화 금지, 할 게 없으면 텍스트 보고만.

### 주제 선정 근거 (수익화 우선순위 관점)
- 5-1 수익화 정책상 **오토 리파이낸스 제휴가 단가 최상위($60~150/성사)**. 따라서 리파이낸스 의도 트래픽을 끌어오는 콘텐츠가 최우선이라고 판단.
- 기존 사이트 전수 확인 결과, **OBBBA 오토론 이자공제($10,000, 2025~2028)를 다룬 전용 페이지가 0개**. 7개 페이지(how-much-car-can-i-afford, should-you-pay-cash-or-finance-a-car, car-loan-calculator, ev-lease-vs-buy-2026, ev-tax-credit-2026, gas-vs-ev-savings-calculator 등)에 **문단 1개씩만 언급**돼 있는 상태 — 7/22 세션의 "보강 1건"이 전부였음. 진짜 갭 확인.
- 시효성: 2026 과세연도부터 Form 1098-VLI 발급 의무화, 공제는 2028년 종료 예정 → 지금이 검색수요 상승 구간.

### 경쟁 회피 장치 (웹서치 3라운드로 확인)
- 헤드텀 "car loan interest deduction (calculator)"은 **TurboTax/H&R Block/US Bank + 전용 도메인(notaxon.com, vehicleloaninterest.com, ustax.tools, trumptaxtools.com)으로 포화 → 정면 경쟁 회피**.
- **"VIN으로 미국 조립 여부 확인" 앵글도 기각** — 딜러 블로그(Ford/Holler Ford/Phillips Buick GMC 등) + 전용 사이트로 이미 포화.
- 대신 **세무 사이트가 안 다루는 "차량 구매 의사결정" 각도로 우회**: 리파이낸스와의 상호작용 / 다년도 실질가치 / 대출을 늘려야 하는가. 우리 사이트의 기존 권위(계산기·구매 의사결정)와 결이 맞고, 세무 사이트는 이 프레임을 쓰지 않음.
- 롱테일 타깃 쿼리: "does refinancing affect car loan interest deduction", "can you deduct interest on a refinanced car loan", "how much is the car loan interest deduction worth", "should i put less down for the tax deduction".

### 검증된 법령 사실 (다음 세션에서 재사용 가능, 출처 다중 교차확인)
- 상한 연 $10,000, 과세연도 2025~2028. 항목별공제 여부 무관하나 **AGI를 낮추지는 않음**(Schedule 1-A, below-the-line). 신고 시 VIN 기재 필수.
- 요건: 신차(최초 소유자) / 미국 최종조립 / 개인용 / GVWR 14,000파운드 미만 / 2024-12-31 이후 오리지네이션 / 차량 1순위 담보. **리스·중고차·특수관계자 대출·샐비지 타이틀·플릿은 전부 제외.**
- 페이즈아웃: MAGI $100k(단독)/$200k(부부합산) 초과분 $1,000당 $200 감액. **감액이 $10,000 상한이 아니라 "실제 공제액"에서 차감되므로, 통상 대출자는 $150k/$250k 훨씬 이전에 0이 됨** — 이게 이번 콘텐츠의 핵심 차별 포인트.
- 리파이낸스: **기존 적격 대출을 리파이하면 자격 유지.** 단 (1) 신규 대출이 동일 차량 1순위 담보이고 (2) 신규 대출 개시잔액이 기존 대출 종료잔액을 초과하지 않을 것. 초과분(캐시아웃) 이자는 공제 불가. **비적격 대출(2025년 이전 오리지네이션, 중고차)은 리파이해도 적격이 되지 않음.**
- Form 1098-VLI: 연 $600 이상 시 대출기관 발급. 2025년은 Notice 2025-57 경과규정, **2026년 이자분부터 의무화**.
- ⚠️ 검색 중 stevenjcpa.com이 페이즈아웃을 $75k/$150k로 기재했으나 **다수 출처와 불일치하는 이상치라 채택하지 않음**. 재확인 시 주의.

### 신규 툴 — `tools/car-loan-interest-deduction-calculator.html`
- 대출금/APR/기간/첫납입월 + 신고구분/MAGI/한계세율/적격여부 입력 → **2025~2028 연도별 이자·공제·절세액 테이블** 출력.
- **차별화**: 경쟁 계산기는 전부 "단일 연도" 계산. 이건 상환스케줄 전체를 돌려서 (a) 2028년 이후 지급이자(영구 공제불가) (b) 페이즈아웃으로 날아간 금액 (c) 총이자 중 실제 공제 비율까지 분해해서 보여줌.
- 검증: 파이썬 + node 목업 DOM 이중 실행 결과 완전 일치. 기본값($42,000/7.2%/60개월/2026-01/단독 MAGI $85,000/22%) → 월납 $836, 총이자 $8,137, 공제 $6,708(82%), 절세 $1,476, 2028년 이후 이자 $1,429. 페이즈아웃은 공표 예시(단독 $120k·이자 $8,000 → 공제 $4,000)와 일치 확인.

### 신규 블로그 3건 (전부 1,000단어 이상)
1. `blog/does-refinancing-affect-car-loan-interest-deduction.html` (Financing, 1,257단어) — **리파이낸스 제휴 유입 목적의 핵심 페이지.** 자격 유지 2요건, 캐시아웃 함정, 기간연장 시 2028년 밖으로 밀리는 문제. 워크드 이그잼플: 잔액 $35,000/48개월, 11.5%→6.9% 리파이 시 이자 $3,678 절감 vs 공제 세후가치 $746 손실 = **순이익 $2,932**. "공제 지키려고 비싼 대출 유지하지 말라"는 결론.
2. `blog/how-much-is-car-loan-interest-deduction-worth.html` (Financing, 1,021단어) — $10,000 헤드라인이 아닌 실제 가치. 4단계 감액(한계세율 / 실제이자 / 2028 절벽 / 페이즈아웃). MAGI $110k에서 총공제가 $1,038로 붕괴하는 표가 핵심.
3. `blog/should-you-borrow-more-for-car-loan-interest-deduction.html` (Financing, 1,104단어) — 미신 반박 4종(계약금 축소/기간연장/현금대신 대출/중고대신 신차). $42k→$47k 시 이자 $969 추가 vs 절세 $176 = **순손실 $793**. 48→84개월 시 절세 $331 늘리려고 이자 $5,130 추가.

### 사이트 전체 반영 내역
- `blog/index.html`: Latest 최상단 3건 추가(23→26개 — **트리밍 여전히 미적용**), Financing 카테고리 섹션에도 3건 추가.
- `tools/index.html`: Financing 섹션에 계산기 카드 추가(car-refinance-calculator 바로 뒤).
- `index.html`: 최신 블로그 미리보기 3개 전면 교체, 툴 그리드 카드 1개 추가, 스탯 카운터 "28+"→"29+" 2곳.
- `sitemap.xml`: 신규 4 URL(102→106), lastmod 12건 갱신. `llms.txt`: Tools 1건 + Guides: Car Financing 3건 추가.
- **내부링크(7/15 교훈)**: 기존 10개 페이지의 Related Guides에 신규 페이지 링크 삽입 — how-much-car-can-i-afford, should-you-pay-cash-or-finance-a-car, how-does-car-loan-interest-work, how-to-refinance-a-car-loan, how-much-should-i-put-down-on-a-car, is-72-month-car-loan-bad-idea, car-loan-calculator, car-refinance-calculator, car-down-payment-calculator, cash-vs-finance-car-calculator. 해당 10개 파일 `dateModified`도 전부 갱신.
- 스크립트로 확인한 인바운드 링크 수: 계산기(8), how-much-is-worth(8), should-you-borrow-more(8), does-refinancing(6).
- ⚠️ **Related Guides 헤딩이 파일마다 "Related Guides" / "Related Guides & Tools" 두 가지로 갈려 있음** — 일괄 스크립트 편집 시 정규식에 둘 다 넣을 것(이번에 1차 스크립트가 6개 파일을 놓쳤다가 2차로 처리함).

### 검증
- 변경/신규 19개 파일: div/p/ul/ol/li/a/table/tr/td/th/select/option/h1/h2/h3/span/tbody/thead/button/script/style/label/strong/em 태그 밸런스 스크립트 확인 — 전부 통과.
- JSON-LD 전 블록 파싱 통과, sitemap.xml XML 파서 유효성 통과(106 URL).
- 사이트 전체 .html 내부링크 895개 전수 스캔 — 깨진 링크 0건. (단, `assets/partials/*.html`의 `{{BASE}}` 6건은 components.js가 치환하는 플레이스홀더라 정상, 스캐너 오탐이니 다음에도 무시할 것.)
- 계산기 JS: node 목업 DOM 실행 + 파이썬 독립 구현 대조, 전 시나리오(기본값/MAGI 110k/130k/비적격/84개월) 수치 일치.

### 6-13-A. 같은 세션 후반부: 실제 GSC/GA 자료 수신 → 분석 + 색인된 페이지 보강

- 사용자가 뒤늦게 자료 첨부(Coverage 드릴다운 2종, Performance 1종, GA4 개요 CSV). **분석 결과는 위 5번 섹션에 전면 반영** — 핵심은 미색인 81개가 "한 번도 크롤링된 적 없음(1970-01-01)"이라는 사실.
- 이 발견에 따라 **작업 대상을 "이미 색인된 17개 페이지"로 전환하여 추가 작업 수행**(신규 발행은 이미 완료된 상태라 확장 기조와 충돌 없음):
  - **보강 — `blog/what-is-good-interest-rate-car-loan.html`** (색인됨, 19.16위, 금리 쿼리 군집 8개가 17~20위에 형성 중). "이자공제 반영 실효 APR" 섹션 신설: Super Prime 4.55%→3.74%, Prime 6.23%→5.14%, Near Prime 9.67%→8.02%, Subprime 13.44%→11.21%(각 -0.81~-2.23%p). 파이썬 이분법으로 실효 APR 역산 검증($42,000/60개월/2026-01/22% 세율, 공제비율 약 83%). 신차 전용이라는 점과 페이즈아웃 경고를 하이라이트 박스로 명시. 1,871→2,026단어.
  - **색인된 페이지 5곳에서 신규 클러스터로 링크 추가**: what-is-good-interest-rate-car-loan, how-to-get-pre-approved-car-loan, how-to-negotiate-car-price-at-dealership, car-depreciation-calculator, used-car-value-calculator. 이로써 신규 4건의 **"색인된 소스로부터의" 인바운드 링크**가 각 3~8개 확보됨(전체 인바운드는 7~11개).
  - sitemap lastmod 5건 추가 갱신, 해당 파일 dateModified 갱신, 태그밸런스·JSON-LD 재검증 통과.
- **다음 세션에 반드시 이어서 할 것**: 색인된 17개 페이지 중 아직 손대지 않은 곳(car-depreciation-calculator 57.31위, used-car-value-calculator 66.74위, mpg-calculator 53.53위, ev-charging-cost-calculator 41.03위, fuel-cost-calculator 42.97위)의 보강 여지 검토. **단, car-insurance-estimator(1,079노출/85.6위)는 방치 정책 유지.**

### ⚠️ 다음 세션 필독
0. **🚫 색인 생성 수동 제출 제안 금지** — 위 5번 섹션 결론 4번 참고. 실효 없음이 확인됐고 사용자가 반복 제안을 명시적으로 기각함.
1. ~~**GSC 자료 첨부 3연속 실패**~~ — 세션 후반 수신 완료 — 세션 시작 시 uploads 폴더부터 확인하고, 없으면 바로 알릴 것.
2. **AdSense 재검토 결과 여전히 미확인**(7/13 제출 이후 4주 이상). 다만 5-1 정책상 승인돼도 현 트래픽에선 실익 없음 — 확인만 하고 재심사 재제출은 하지 말 것.
3. 8/11 신규 4건의 색인 여부를 다음 GSC 확인 시 포함해서 볼 것. 특히 **Financing 클러스터는 사이트에서 가장 내부링크가 촘촘한 신규 묶음**이라 색인 속도 비교 대조군으로 쓸 가치가 있음.
4. **이 클러스터는 2028년 시효성 콘텐츠** — 의회가 연장하지 않으면 2029년 이후 가치가 급락. 또한 **연 1회는 IRS 가이던스 재확인 필요**(Form 1098-VLI 서식 확정, Schedule 1-A 변경, 페이즈아웃 인플레이션 조정 여부). EV 등록세·관세 계산기와 같은 시효성 관리 대상에 추가.
5. blog/index.html Latest가 26개로 증가 — 트리밍(캡핑) 여부 **사용자 확인 필요**. 7/19에 처음 제안한 이후 5세션 연속 미결 상태.
6. **리파이낸스 제휴 도입 시 이 클러스터가 최적 배치 지점** — `does-refinancing-affect-car-loan-interest-deduction.html`과 `tools/car-refinance-calculator.html`이 의도 가장 높은 페이지. 트래픽 임계치 도달 시 Caribou/RefiJet/myAutoloan 링크를 여기부터 넣을 것(FTC 고지 문구는 이미 editorial-policy.html에 준비돼 있음).
7. 이번에 기각한 주제: VIN 미국조립 확인(딜러 블로그 포화), 이자공제 일반 가이드(TurboTax/HRBlock 포화) — 향후 재검토 불필요.


## 6-14. 8/18 세션 (일요일 주간 루틴): Bing 데이터 최초 분석 → MPG 클러스터 집중 + 주 간 구매 신규

- **첨부 자료**: GSC Coverage 2종·Performance 1종, GA4 개요, **Bing Webmaster Tools 2종(PageTrafficReport, KeywordReport) 최초 제공**. `freetooldev_com` 폴더도 zip에 섞여 있었으나 **다른 사이트라 분석에서 제외**(다음에도 혼입 가능하니 주의).
- **분석 결과는 5번 섹션에 전면 반영.** 핵심은 "Bing은 잘 색인하고 1~10위에 올려준다" — 구글 크롤링 병목이 콘텐츠 문제가 아님을 2차 확정.

### 작업 선정 근거
- Bing 노출의 **62%가 `what-is-a-good-mpg-for-a-car.html` 한 페이지(89노출/5.17위)**에 몰려 있음. GA4 조회수도 홈 다음 2위. **사이트에서 가장 검증된 트래픽 자산**이므로 여기에 집중하는 것이 최우선.
- Bing 키워드에 **"is 23 mpg good" 형태의 숫자 진입 쿼리가 반복 등장**(19/23/24/38). 기존 페이지는 차종별 표만 있고 **숫자로 들어오는 사용자에게 직접 답하는 구조가 없었음** — 정확한 갭.
- 경쟁 확인(웹서치 2라운드): gizmodriver.com, calendar-canada.ca, fuelconsumptioncalc.com 등 **소형 사이트가 상위** → 규칙 4 기준 기회. NerdWallet/Bankrate급 없음.

### 보강 1 — `blog/what-is-a-good-mpg-for-a-car.html` (최우선, Bing 89노출/5.17위)
- **"Is My MPG Good? Look Up Your Exact Number" 섹션 신설** — 15~40+ MPG를 행으로 두고 각 숫자가 어느 차종에 좋고 나쁜지 역방향 매핑 + 연간 연료비. 기존 차종별 표를 소스로 파이썬 매트릭스 생성해 **모순 없음을 검증**.
- "23 MPG가 힌지 포인트"(그 아래는 트럭/SUV 기준으로 관대하게, 위는 세단/하이브리드 기준으로 엄격하게 평가됨)라는 인사이트 추가. 왜 같은 숫자에 상반된 답이 나오는지 설명하는 섹션도 신설.
- **메타 교체**(CTR 0% 대응): title에 "Look Up Any Number (2026)", description에 "Is 19, 23, 24, or 38 MPG good?" — Bing 실제 쿼리 숫자를 그대로 반영. 1,368 → 1,903단어.

### 보강 2 — `tools/mpg-calculator.html` (구글 61노출/57위 + Bing 색인)
- 기존 판정은 **차종 무관 고정 임계값**(40/30/22)이라 블로그가 지적하는 오류를 툴이 저지르고 있었음 → **차종 선택 9종 + 연간주행거리 + 유가 입력 추가**, 클래스별 판정으로 교체.
- 판정 문구에 "같은 숫자가 다른 차종에선 어떻게 평가되는지"까지 출력. node 목업 DOM으로 6개 시나리오 실행 → **블로그 룩업 표 및 파이썬 계산과 전부 일치 확인**(23MPG 픽업=Good/컴팩트세단=Poor, 38MPG 하이브리드=Poor, 연료비 $2,152·$2,605·$1,303 일치).

### 신규 블로그 1 — `blog/is-a-high-mpg-car-worth-the-extra-cost.html` (Running Costs, 1,117단어)
- Bing **최다 쿼리 "are car with high mpg good"(7노출/4위)** 직접 대응. 기존 파일 전수 확인 결과 gas→gas 연비 업그레이드 페이백 각도는 없었음(gas-vs-ev는 EV 비교, how-to-improve-gas-mileage는 운전습관).
- 핵심: **MPG 비선형성**. 15→20 MPG는 연 $825 절약인데 35→40은 $177 — **같은 5 MPG인데 4.7배 차이**. GPM(100마일당 갤런) 표로 선형 비교법 제시.
- 페이백 표(프리미엄 $2,000/$3,500/$5,000 × 4개 업그레이드), 주행거리별 민감도(8,000~30,000마일). "연비 절약으로 더 비싼 차 할부금을 못 메운다"($47/월 vs $99/월) 결론. Forbes 인용치(25→35 MPG, $4 가스 = 월 $57)와 계산 일치 확인.

### 신규 블로그 2 — `blog/does-buying-a-car-out-of-state-save-on-taxes.html` (Buying, 1,302단어)
- Bing 쿼리 "MN에서 사서 AZ에 등록 vs AZ에서 사기"(3노출/6위) 직접 대응. 전용 페이지 없었고 계산기에 한 문장만 있던 갭.
- 경쟁(legalclarity.org, nextgenauto.us, carflipiq.com 등)은 전부 **세율표 나열형**이라, 우리는 **의사결정 각도**로 우회.
- 검증된 사실: 세금은 **등록지(거주 주) 기준**, 상호 크레딧은 홈 주 세액 한도라 **초과분 환급 없음**(AZ 홈 + MN 6.5% 징수 시 $315 손실). 무세금 5주(AK/DE/MT/NH/OR) 구매도 홈 등록 시 총액 동일($2,812), 다만 **딜러 파이낸싱 대신 DMV 현금 납부로 바뀜**. **트레이드인 크레딧 상실이 실제 결정타**($784~$1,015). 캘리포니아는 애초에 트레이드인 크레딧이 없어 예외.

### 보강 3 — `tools/car-sales-tax-calculator.html` (Bing 10노출/6.20위)
- "Buying Out of State: Which Rate Applies?" 섹션 추가 + 신규 블로그로 링크.

### 사이트 전체 반영
- `blog/index.html` Latest 최상단 + Buying a Car·Running Costs 카테고리 각각 추가.
- `index.html` 미리보기 3개 교체(신규 2 + 이자공제 1). 툴 신규 없어 stat 숫자는 29+ 유지.
- `sitemap.xml` 106→108 URL, lastmod 10건. `llms.txt` Running Costs·Buying a Car 섹션에 각 1건.
- **내부링크: 실제 크롤링되는 12개 페이지에서만** 신규 글로 링크(구글 노출 17개 + Bing 노출 13개 집합 기준). 인바운드 high-mpg 10개, out-of-state 7개.

### 검증
- 변경/신규 17개 파일 태그 밸런스(select/option/button 포함) 전부 통과, JSON-LD 전 블록 파싱 통과, sitemap XML 유효(108 URL).
- 사이트 전체 내부링크 930개 전수 스캔 **깨진 링크 0건**(`assets/partials`는 `{{BASE}}` 플레이스홀더라 스캔 제외 — 이번엔 스캐너에서 아예 걸러내도록 수정함).
- MPG 계산기 JS는 node 실행으로 판정·연료비를 파이썬 및 블로그 표와 대조 완료.

### ⚠️ 다음 세션 필독
1. **Bing KeywordReport를 매번 우선 분석할 것.** 구글 쿼리는 정체돼 새 정보가 없는 반면 Bing은 실제 검색어를 보여주는 유일한 소스가 됨.
2. **MPG 페이지 메타 교체의 CTR 효과를 반드시 확인.** 89노출/5.17위에서 클릭이 나오기 시작하면 **다른 Bing 상위 페이지(how-much-should-i-put-down 6.75위, car-sales-tax-calculator 6.20위, ev-registration-fees 7.88위)에도 같은 방식으로 메타 최적화를 확대**할 것. 이게 현재 가장 저비용·고효율 트랙.
3. 8/11 신규 4건은 일주일간 구글 크롤링 0. **Bing에서는 잡히는지 다음 리포트에서 확인**할 것.
4. `what-is-good-interest-rate-car-loan`의 실효 APR 섹션(8/11 추가)이 아직 구글 미반영 — 순위 변화 추적할 것.
5. zip에 `freetooldev_com` 폴더가 섞여 있었음. **다른 사이트이므로 분석에 포함하지 말 것.** 사용자가 그 사이트 작업을 원하면 별도 지시가 있을 것.
6. blog/index.html Latest 섹션이 계속 증가 중(트리밍 여부 6세션째 미결). 사용자 확인 필요.


## 6-15. 8/24 세션 (사용자 지시: 신규 위주, 폭넓은 키워드 리서치): 신규 클러스터 "Accidents & Claims" 신설

- **지시 사항**: 신규 중심. 키워드를 다양하게 폭넓게 뽑고 → 리스트 → 경쟁강도 체크 → 강하면 롱테일로 우회. 가급적 클러스터 단위, 새 클러스터도 환영. **GSC/보유 데이터 안에서만 보지 말고 구글·네이버·레딧 등에서 "문서수는 적은데 관심은 있는" 주제를 찾을 것.** 화면 깨짐 확인 필요한 페이지만 링크로 전달.
- **이번엔 GSC/GA/Bing 자료 첨부 없음** — 지시대로 외부 소스 리서치 기반으로만 진행. 8/18자 데이터 판단(5번 섹션)은 그대로 유효.

### 리서치 → 후보 리스트 → 경쟁강도 판정 (웹서치 5라운드)
전체 콘텐츠 69개 전수 대조로 **완전 미커버 영역**을 먼저 특정: 사고/클레임, 압류/자진반납, 청소년 운전자, 클래식카, 견인/적재, IRS 마일리지 공제, 차량 기부, 겨울 타이어.
그중 (a) 계산 가능하고 (b) 기존 툴과 로직이 안 겹치고 (c) 수익화 궁합이 맞는 **사고/클레임 + 압류**를 선택. 후보별 경쟁강도:

| 후보 | 상위 노출 | 판정 |
|---|---|---|
| 사고 후 보험료 인상률 | NerdWallet·ValuePenguin·WalletHub·LendingTree·US News | **포화 → 기각** |
| total loss threshold by state (주별 표) | Policygenius·WalletHub·SoFi·carinsurance.com | 표는 코모디티화 → 헤드텀 회피 |
| 17c 감가상각 계산기 | The Zebra·toolcr·cdcalculators·secondappraisal·snapclaim | 계산기 자체는 포화 → **각도 전환** |
| total loss 계산기 | The Zebra·calculator.academy·collisionhelp·mycarcalc | 포화 → **각도 전환** |
| 자진반납 deficiency | NerdWallet·Chase·CapitalOne·Nolo·Experian(설명글) | **계산기는 0개 → 진입** |

### 경쟁 회피 장치 (전부 "설명"이 아니라 "의사결정 + 계산"으로 우회)
- **전손**: 경쟁사는 "전손인가?"에서 멈춤 → 우리는 **공제액 차감 후 실수령 → 대출 상환 가능 여부 → 잔존물 인수 시 총비용**까지 끝까지 계산.
- **감가상각(DV)**: 경쟁사는 17c 숫자만 뱉음 → 우리는 **자격 게이트(1st-party 면책이라 대부분 청구 불가)** 를 앞에 세우고 **감정료 $300~400 대비 손익분기**를 계산. 이게 진짜 결정 변수인데 아무도 안 다룸.
- **자진반납**: 설명글만 존재 → 우리는 **경매가 vs 직접매각 부족액 차이**를 수치화.

### 신규 툴 — `tools/totaled-car-settlement-calculator.html` (873단어)
- 입력: ACV, 수리비, 잔존가, 주 규칙(60~100% 임계 또는 TLF), 공제액, 과실 주체, 대출잔액, 갭 보유.
- **기존 `gap-insurance-calculator`와 로직 미중복 확인**(그쪽은 사전적 "갭보험 살까?", 이쪽은 사고 후 정산). 규칙 4 준수.
- 3분기 출력: 전손 판정 / 정산 내역(ACV−공제−대출) / **오너 리텐션 비교**(포기 정산액 + 자가수리비 vs 리빌트 타이틀 가치 20~40% 하락).
- 검증: 파이썬 독립 구현 + node 목업 DOM 6시나리오 대조 **전부 일치**. TLF 케이스($13,000+$4,500=$17,500 < ACV $18,000 → 수리) 포함.
- UX 보정 2건: 기본값을 전손 시나리오로($15,000 수리비 → 83%), 수리 판정 시 정산 카드 자동 숨김.

### 신규 블로그 3건
1. `blog/should-you-keep-your-totaled-car.html` (Accidents & Claims, 1,196단어) — **오너 리텐션은 검색량 대비 문서가 가장 적은 지점.** ACV $18,000/수리 $15,000/잔존 $4,500 기준 총 $19,500 써서 $10,800~$14,400짜리 차를 갖게 됨. 리텐션이 통하는 5가지 경우(센서發 전손, 저가차, 우박, 자가수리, 평생보유)와 실무 장애물(재보험 거절, 렌더 차단, 검사 탈락, 히든 데미지 무보증) 정리. 기존 `is-it-worth-buying-car-with-rebuilt-title`의 정확한 뒷면이라 내부링크 궁합 최상.
2. `blog/is-a-diminished-value-claim-worth-filing.html` (Accidents & Claims, 1,206단어) — 자격 게이트 5종을 먼저 세움(**핵심: 대부분 약관이 1st-party DV를 면책 → 상대 과실일 때만 청구 가능, 조지아는 Mabry 판결로 예외**). 17c 표($28,000 기준 손상×주행거리 12칸) + 감정료 $350 손익분기표. 85,000마일이면 중간 손상도 적자.
3. `blog/should-you-sell-your-car-instead-of-voluntary-surrender.html` (Financing, 1,102단어) — 잔액 $23,000/시세 $16,000 기준 자진반납 부족액 $12,300 vs 직접매각 $7,000 = **차이 $5,300 + 7년 신용기록 회피**. 부족액 브리징 3방법, 그 전에 시도할 것(리파이낸스·디퍼먼트·트레이드다운), 이미 반납한 경우 무담보채무化로 협상 가능.

### 수익화 관점 우선순위 (5-1 정책 적용)
- 3번 블로그가 **리파이낸스 제휴(단가 최상위 $60~150)** 와 직결 — "연체 전이면 리파이낸스가 답"이라는 구조로 `car-refinance-calculator`·`how-to-refinance-a-car-loan`에 링크. 압류 직전 사용자는 의도가 극도로 높음.
- 1·2번은 `used-car-value-calculator`·중고차 인스턴트 오퍼(Peddle/CarMax) 제휴와 궁합. **단, 보험 쇼핑 제휴는 여전히 방치**(우리 보험 페이지 85위, 5-1 판단 유지).

### 사이트 전체 반영
- **blog/index.html에 `🚨 Accidents &amp; Claims` 카테고리 섹션 신설**(id=`section-accidents`, Gig & Rideshare 뒤). Latest에 3건, Financing에 1건 추가.
- **tools/index.html에도 동일 카테고리 신설**(Electric Vehicles 앞) + 계산기 카드.
- index.html 미리보기 3건 전면 교체, 툴 그리드 카드 추가, stat `29+`→`30+` 2곳.
- sitemap 108→112 URL(lastmod 13건), llms.txt `## Guides: Accidents & Claims` 섹션 신설 + Tools 1 + Financing 1.
- 내부링크 13개 페이지에서 연결. **구글/Bing 노출 확인된 페이지 우선**(used-car-value 64노출, car-depreciation 128노출, negative-equity Bing 2.88위, put-down Bing 6.75위). 인바운드 5~9개 확보.

### 검증
- 변경/신규 17개 파일 태그 밸런스·JSON-LD 전부 통과, sitemap XML 유효(112 URL).
- 내부링크 980개 전수 스캔 깨진 링크 0건.
- 계산기 JS 파이썬 대조 완료.

### ⚠️ 다음 세션 필독
1. **Accidents & Claims는 이번에 씨앗만 심은 상태.** 확장 후보(리서치는 했으나 이번엔 미발행): 사고 후 렌터카 커버리지, ACV 이의제기 실무(appraisal clause), 우박 피해 전손, 무보험 운전자 사고. **단 "사고 후 보험료 인상률"은 포화라 기각했으니 재검토 불필요.**
2. **여전히 미커버인 영역**(다음 클러스터 후보): IRS 사업용 마일리지 공제(시즌성 큼), 청소년/신규 운전자 비용, 차량 기부 세금공제, 견인·적재량, 겨울타이어. 전부 이번에 리스트만 뽑고 미착수.
3. 8/18에 교체한 MPG 페이지 메타의 **CTR 효과 확인이 여전히 최우선** — Bing 89노출/5.17위. 효과 확인되면 다른 Bing 상위 페이지로 확대.
4. blog/index.html Latest 섹션 트리밍 여부 7세션째 미결.


## 6-16. 8/31 세션 (사용자 지시: 신규 위주, 폭넓은 키워드 리서치): 신규 클러스터 "Moving & Relocation" 신설 + EV 확장

- **지시**: 신규 중심, 키워드 폭넓게 → 리스트 → 경쟁강도 → 강하면 롱테일 우회. 클러스터 단위, 새 클러스터 환영. GSC/보유 데이터 밖(구글·네이버·레딧 등)에서 문서수 적고 관심 있는 주제 발굴. 화면 깨짐 확인 필요한 페이지만 링크.
- **GSC/GA/Bing 자료 첨부 없음** — 지시대로 외부 리서치만으로 진행. 8/18자 데이터 판단(5번 섹션) 그대로 유효.

### 후보 리스트 → 경쟁강도 판정 (웹서치 4라운드)
6-15에서 리스트만 뽑아둔 미커버 영역부터 착수. 판정 결과:

| 후보 | 상위 노출 | 판정 |
|---|---|---|
| 차량 배송비(ship a car) 헤드텀 | RoadRunner·Sherpa·Nexus·AmeriFreight(브로커 리드젠) + Forbes·ConsumerAffairs | **포화 → 기각** |
| **배송 vs 직접운전 결정** | Forbes·Move.org가 얕게 언급, **전용 계산기 0개** | **진입** |
| EV 배터리 수명/교체비 헤드텀 | ConsumerAffairs·SoFi·Recurrent·다수 소형 | 포화 → 각도 전환 |
| **워런티 만료 중고 EV 리스크 가격화** | 아무도 의사결정·기대값으로 안 다룸 | **진입** |
| 10대 운전자 보험 | MoneyGeek·CarInsurance·Insurify·Progressive·Bankrate 전부 계산기 보유 | **기각**(+ 보험 방치 정책) |
| 주 간 이전 시 차량 등록 절차 | 주별 DMV·이사업체 산발적, 통합 의사결정 문서 없음 | **진입** |

### 경쟁 회피 장치
- **배송**: 업계 콘텐츠는 전부 "배송비 얼마"에서 끝남 → 우리는 **반대편(직접운전)을 정직하게 가격화**. 숙박·식비·마모·편도항공·**시간가치**까지 넣으니 결론이 뒤집힘.
- **EV 배터리**: 경쟁사는 "평균 열화율/교체비" 나열 → 우리는 **기대값 계산**(교체비 × 고장률 vs 중고 할인폭)으로 의사결정화.
- **주 간 이전**: 주별 표 나열 회피 → **처리 순서(보험 먼저 → 검사 → 등록 → 면허)** 로 구성. 순서 틀리면 DMV 재방문이라는 게 핵심.

### 신규 툴 — `tools/ship-car-vs-drive-calculator.html` (871단어)
- 입력: 거리/캐리어종류/차량크기/가동여부/실제견적(선택)/편도항공 + MPG·유가·호텔·식비·일일운전시간·**시간가치**·마모비.
- **핵심 발견**: 현금비용만 보면 운전이 거의 모든 구간에서 저렴. **시간가치가 답을 결정** — 시급 $0이면 대륙횡단도 운전 우세, $25면 손익분기 1,500마일, $40이면 1,000마일.
- 결과에 **"당신의 시간이 시급 얼마 이상이어야 배송이 유리한지"** 를 역산해서 표시(경쟁사 전무).
- per-mile 곡선은 `0.45 + 2.6/(1+miles/260)` 로 **단조 감소·연속** 처리(계단식 요율표는 300mi가 600mi보다 비싸지는 역전이 생겨 폐기).
- 검증: 파이썬 독립 구현 + node 목업 DOM 6시나리오 일치. 1,500mi/시급$25에서 차이 $31 = 손익분기 근처로 파이썬 결과와 부합.

### 신규 블로그 3건
1. `blog/should-you-ship-your-car-or-drive-it.html` (Moving, 1,016단어) — 1,500마일 기준 운전 현금 $965 vs 배송 $1,501, 그러나 운전은 24시간 소요. 시간가치별 손익분기표. 브로커 입찰 구조·견적 편차 이유·개인물품 100파운드 미보험 등 실무.
2. `blog/moving-to-another-state-what-to-do-with-your-car.html` (Moving, 1,202단어) — **보험 먼저** 순서 논리, 20~60일 데드라인, 검사/배출가스가 등록을 막는 구조, 융자차는 렌더 타이틀 요청에 수주 소요, 군인 SCRA·유학생 예외. 판매세는 재과세 안 됨(기존 out-of-state 글과 차별).
3. `blog/should-you-buy-a-used-ev-out-of-battery-warranty.html` (EV, 1,103단어) — Geotab 22,700대 열화 2.3%/yr(최신팩 1.8%), 8년차 SOH 83%, 70% 도달 ~15년. 팩 크기별 교체비표. **기대값**: 할인 $5,000 + 연료절약 $3,763 − 리스크 $225 = **+$8,538**, 단 최악 시 −$2,487(꼬리 위험 명시). 주행거리보다 충전이력·기후가 중요.

### 사이트 반영
- blog/index.html·tools/index.html에 `🚚 Moving &amp; Relocation` 카테고리 신설, Latest 3건, EV 섹션 1건.
- index.html 미리보기 3건 교체 + 툴카드, stat `30+`→`31+` 2곳.
- sitemap 112→116 URL(lastmod 14건), llms.txt `## Guides: Moving & Relocation` 신설 + Tools 1 + EV 1.
- 내부링크 14개 페이지. **구글/Bing 노출 확인 페이지 우선**(ev-charging 46노출, fuel-cost 42노출, gas-vs-ev 27노출, road-trip 11.5위, ev-registration Bing 7.88위, car-sales-tax Bing 6.20위). 인바운드 6~9개.

### ⚠️ 이번에 실제로 발생한 사고 (재발 방지)
- **블로그 3건 생성 시 템플릿 CSS를 `sed -n '13,45p'` 로 줄번호 추출했다가 gtag 스크립트와 JSON-LD 조각까지 삼킴** → 3파일 모두 `<style>` 안에 스크립트가 박히고 JSON-LD가 깨짐. **규칙 7 검증에서 잡아냄**(script 10/9 불균형 + JSON 파싱 실패).
- 교훈: **템플릿 조각은 줄번호가 아니라 정규식 경계로 추출할 것** (`re.search(r'<style>\n(.*?)\n  </style>', src, re.S)`). 추출 직후 `assert 'gtag' not in css` 같은 오염 검사를 넣을 것.
- 복구 후 재검증 전부 통과.

### 검증
- 변경/신규 18개 파일 태그 밸런스·JSON-LD 통과, sitemap XML 유효(116 URL), 내부링크 1,028개 전수 스캔 깨짐 0건.

### ⚠️ 다음 세션 필독
1. **Moving & Relocation 확장 후보**(리서치는 했으나 미발행): 이사 시 렌터카/트레일러 견인 비용, 스냅버드 계절 이전, 해외 파병·이주 시 차량 처리. **단 "차량 배송비 얼마"는 브로커 리드젠 포화라 재검토 불필요.**
2. **여전히 미커버**(다음 클러스터 후보): IRS 사업용 마일리지 공제(시즌성 큼 — 연초 발행이 유리), 차량 기부 세금공제, 견인·적재량, 겨울타이어. 10대 운전자 보험은 8/31에 포화 확인해 기각.
3. Accidents & Claims 확장 후보(6-15에서 이월): 사고 후 렌터카 커버리지, ACV 이의제기 실무, 우박 전손, 무보험 운전자 사고.
4. **MPG 페이지 메타 CTR 효과 확인 여전히 미확인** — Bing 89노출/5.17위. GSC/Bing 자료 받으면 최우선.
5. blog/index.html Latest 트리밍 여부 8세션째 미결.


## 6-17. 9/7 세션 (주간 루틴): 노출 폭락 원인 규명 + MPG CTR 수정 + 리스 초과주행 신규

- **첨부**: GSC Coverage 2종·Performance 1종(8/24자), GA4 개요, Bing 2종. zip에 8/11·8/18 과거분과 `freetooldev_com` 폴더가 섞여 있었으나 **다른 사이트라 제외**(3회 연속 혼입 — 다음에도 무시).
- 분석 결과는 5번 섹션에 전면 반영. 핵심 3가지: **노출 폭락은 5월 스파이크 윈도우 이탈**, **스파이크 제거 후 진짜 순위는 5~9위권**, **Bing 최초 오가닉 클릭 2건**.

### 작업 1 (최우선) — `blog/what-is-a-good-mpg-for-a-car.html` CTR 수정
- 근거: Bing **235노출(전체 57%) / 5.48위 / 클릭 0**. 같은 순위대 put-down은 44노출로 1클릭 → 메타 문제 확정.
- **타이틀에 "Average" 추가**: `What Is a Good MPG for a Car? Average MPG & Any Number (2026)`. Bing 최다 쿼리 "what is the average mpg for a car"(14노출)가 기존 타이틀에 없었음.
- 디스크립션도 "The average car gets 26-28 MPG. Is 23, 29, 32 or 36 MPG good?"로 교체 — 관측된 숫자를 직접 노출.
- **"What Is the Average MPG for a Car?" 전용 H2 섹션 신설** — 신차 26~28, 승용차만 32~35, 트럭/SUV 22~26, 도로 위 전체 22~24, 10년차 20~24로 분해. "average"가 어느 average냐에 따라 다르다는 게 핵심.
- **룩업 표에 29/32/36/43/49 추가**(Bing에서 실제 관측된 숫자인데 누락돼 있었음), 40+ 행에 60까지 명시. 기존 차종별 표와 동일 로직으로 파이썬 산출 후 삽입. **삽입 후 숫자 오름차순 재정렬 필요했음**(25→29→28 순서 꼬임 발생 → 스크립트로 정렬).
- 1,903 → 2,141단어.

### 작업 2 (신규) — 리스 초과주행 클러스터
- 근거: 구글 쿼리 `excess mileage charge calculator` 85위 존재하나 **전용 페이지 0개**(기존엔 리스 글 안에 언급만).
- 경쟁 확인(웹서치 1라운드): omnicalculator·goodcalculators·bizcalcs·ezcalculator·yescalculator·calcipedia 등 **범용 얇은 계산기가 다수**. 전부 "초과마일 × 요율" 한 줄 계산에서 끝남.
- **경쟁 회피 각도 — 4가지 출구 비교**: ① 덜 타기(일일 마일 예산 역산) ② 턴인 시 납부 ③ 마일 선구매(요율 절반) ④ **바이아웃 — 구매하면 초과요금이 소멸**. ④는 어느 경쟁사도 계산하지 않음.
- `tools/lease-excess-mileage-calculator.html` (859단어): 연 허용/기간/경과/주행/요율/선구매요율 + 잔존가·시세·수수료·처분수수료. 파이썬 + node 목업 DOM 5시나리오 대조 일치.
- `blog/what-happens-if-you-go-over-lease-mileage.html` (Buying, 1,248단어): 9,000마일 초과 기준 턴인 $2,250 vs 선구매 $1,080. **바이아웃 비교표** — 반납 시 $2,645 지출 + 차 없음 vs 바이아웃 시 $1,650 언더워터지만 **순 $995 유리**. 시세가 바뀌면 결론이 뒤집히므로 계산이 필요하다는 점 명시.
- **기존 툴과 로직 미중복 확인**(`lease-takeover-cost-calculator`는 인수 비용, `car-lease-vs-buy-calculator`는 리스vs구매). 규칙 4 준수.

### 사이트 반영
- blog/index.html Latest + Buying a Car, tools/index.html Buying & Financing 섹션, index.html 미리보기 교체 + 툴카드, stat `31+`→`32+`.
- sitemap 116→118 URL(lastmod 12건), llms.txt Tools 1 + Buying 1.
- 내부링크 10개 페이지. 신규 블로그 인바운드 11개, 계산기 7개.
- **Related Guides 헤딩 `<h2>` 변형(7개 파일) 때문에 1차 스크립트가 3개 파일을 놓침** → 2번 섹션에 3가지 변형 전부 기록해뒀으니 다음엔 한 번에 처리할 것.

### 8/31 사고 재발 방지 확인
- 템플릿 CSS를 **정규식 경계로 추출 + `assert 'gtag' not in css` 오염검사** 적용 → 이번엔 오염 없음. 신규 블로그 script 6/6, style 1/1, JSON-LD 2블록 정상.

### 검증
- 변경/신규 16개 파일 태그 밸런스·JSON-LD 통과, sitemap XML 유효(118 URL), 내부링크 1,057개 전수 스캔 깨짐 0건.

### ⚠️ 다음 세션 필독
1. **MPG 메타 재교체(9/7) 효과 확인이 최우선.** 235노출/5.48위/0클릭이 클릭을 내기 시작하면, 같은 방식을 Bing 상위 페이지에 확대: best-time-of-year-to-buy-a-car(36노출/6.83위 — 8/24에 새로 급부상), how-much-does-car-maintenance-cost-per-year(19노출/5.95위), how-much-does-it-cost-to-fill-up-a-car(15노출/5.07위).
2. **구글 running/expense calculator 군집 7개(84~100위)** — `car-total-cost-of-ownership-calculator` 메타·본문에 "running cost / car expense / vehicle expense" 표현을 넣어 커버리지를 넓히는 작업. 색인된 페이지라 즉시 효과 가능.
3. **`car break even calculator`(5노출, 구글 최다 쿼리)** — 우리에 break-even 전용 계산기 없음. 리스vs구매·리파이낸스·연비업그레이드 등 여러 글에 break-even 개념이 흩어져 있으니 통합 툴 후보.
4. **Bing 신호 중 미커버**: "how much would it affect the trade-in value of a brand new car with 700 miles and $1,000 in repairs"(2쿼리, 5~8위) — 사고이력이 트레이드인에 미치는 영향. 8/24 발행한 `is-a-diminished-value-claim-worth-filing`과 인접하나 **트레이드인 관점 전용 글은 없음**. "average maintenance and tires cost"(타이어 별도 언급)도 미커버.
5. 미착수 클러스터 후보(이월): IRS 사업용 마일리지 공제(연초 발행 유리), 차량 기부 세금공제, 견인·적재량, 겨울타이어. Accidents 확장(렌터카 커버리지·ACV 이의제기·우박 전손), Moving 확장(트레일러 견인·스냅버드).
6. blog/index.html Latest 트리밍 여부 9세션째 미결.


## 9. GitHub 작업 방식 안내 (신규 세션 시작 시 참고)

- 이 저장소는 사용자가 매 세션 GitHub Personal Access Token을 직접 발급해서 대화 중에 전달하는 방식으로 운영됨. 토큰이 없으면 clone은 되지만(public repo) push는 불가.
- 작업 시작 시: `git clone` → `git remote set-url origin https://<username>:<token>@github.com/canghun13/autocalchub.git` → `git config user.email/name` → `git pull`로 최신화 후 작업.
- 작업은 사용자가 명시적으로 지시했을 때만 진행 (규칙 1). 신규 콘텐츠는 방향 보고 후 승인받고 작성 시작 (규칙 4).
- 완료 후 커밋 메시지에 변경 이유와 근거(경쟁 강도 확인 결과, 어떤 GSC 신호 때문인지 등)를 상세히 남길 것 — 다음 세션에서 이 로그가 유일한 판단 근거가 됨.
