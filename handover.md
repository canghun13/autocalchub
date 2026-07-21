# AutoCalcHub 인수인계 문서 (2026-07-21 기준)

> 이 문서는 새 대화 세션에서 이어받아 작업을 진행할 수 있도록 프로젝트 전체 맥락을 담은 통합 인수인계 문서입니다. Git 루트에 위치하며, 작업할 때마다 이 문서를 최신 상태로 갱신할 것.

---

## 1. 사이트 기본 정보
- 도메인: autocalchub.com / GitHub Pages 호스팅 / Cloudflare 관리, 연 $10.46
- 저장소: `github.com/canghun13/autocalchub` (public)
- GA4: G-ZH1JYG24PK
- 애드센스: ca-pub-5592663499707350
- 디자인: 다크 네이비 + 오렌지, 폰트는 Space Grotesk(제목) + Inter(본문)
- 월 운영비: 약 38,000원 (Claude Pro + 도메인 5개)

## 2. 콘텐츠 현황 (2026-07-12 기준)
- 블로그 51개 (`blog/` 폴더, index.html 제외) — 7/17 세션에서 7개 추가(`should-you-pay-cash-or-finance-a-car`, `is-certified-pre-owned-worth-it`, `is-extended-car-warranty-worth-it`, `carmax-vs-carvana-which-pays-more`, `how-to-price-car-for-private-sale`, `how-to-sell-car-with-loan-still-on-it`, `how-to-avoid-scams-selling-car-privately`)
- 툴 22개 (`tools/` 폴더, index.html 제외) — 7/17 3차 세션에서 `cash-vs-finance-car-calculator.html` 추가
- 정적 페이지: `about.html`, `contact.html`, `privacy-policy.html`, **`methodology.html`(신규)**, **`editorial-policy.html`(신규)**
- sitemap.xml 총 URL 81개 (블로그+툴+정적페이지+blog/index+tools/index, 7/17 세션 반영)
- **블로그 태그 카테고리**: Financing / Buying / Running Costs / Ownership / EV / **Selling (7/17 신설)**. Selling은 "판매/처분" 콘텐츠 전용 — 신규 판매 관련 콘텐츠는 이 태그 사용할 것.
- `tools/index.html` — 블로그 인덱스와 동일한 구조(카테고리별 그리드 + 검색기능)로 신규 생성됨 (기존엔 없었음)
- **블로그 44개 전체**에 `<div class="blog-meta">...</div>` 줄에 "· Written by AutoCalcHub Team" 바이라인 통합 반영됨 (7/12) — 신규 블로그 작성 시 이 형식 유지할 것
- **블로그 44개 + 툴 21개 = 65개 페이지 전체**에 BreadcrumbList JSON-LD 스키마 반영됨 (7/12) — 신규 페이지 작성 시 이 패턴(Home > Blog/Tools > 페이지명) 동일하게 추가할 것. FAQPage/HowTo 스키마는 2026-05-07 Google이 리치 리절트를 폐지해서 더 이상 유효한 선택지 아님(추가하지 말 것).

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

## 4. 주간 루틴 (정기 작업, 일요일)
- 매주 일요일: 블로그 3개 + 툴 1개 **신규 또는 보강**
- 작업 시작 전 GA4 + Search Console 리포트 캡처 받아서 방향 잡기
- **정기 루틴과 별개로**, 세션 여유가 있을 때 GSC 데이터 기반 추가 보강/신규 작업을 하기도 함 (7/8, 7/10 세션이 이 케이스) — 이건 "주간 루틴 소진"과 무관하게 별도로 카운트됨

## 5. SEO / Search Console 현황 (2026-07-19 기준 최신 확인 — 실제 GSC export 파일로 확인)
- **노출수**: 5/14~5/20에 하루 200~270회로 급증(보험 키워드 초기 크롤링 테스트성 노출) → 5/21 이후 하루 0~4회로 계속 유지 중(7/17까지 확인, 9주째 동일 패턴). 정상적인 저권위 신규 도메인 baseline으로 계속 판단.
- **클릭수**: 3개월 누적(5/10~7/17) **여전히 0건**. 노출 자체가 워낙 작아서(대부분 페이지 노출 4~183회) 통계적으로 이상 신호 아님 — rule 6 그대로 적용.
- **색인 현황**: Coverage 리포트는 항상 1~2주 지연 반영됨 — 7/19에 받은 리포트도 7/10 데이터까지만 있음. **7/15 내부링크 보강, 7/17 세션들, 7/19 오늘 세션(보강 5개+신규 3개)의 효과는 전부 이 리포트에 아직 반영 안 됨** — 다음 확인은 최소 7/22 이후에.
- **색인 생성됨**: 16개, 6/6부터 지금(7/10 데이터 기준)까지 **5주 이상 정체 그대로**. "발견됨-크롤링대기" 53개 + "크롤링됨-미생성" 2개 = 미색인 55개(7/15 확인 47→55에서 그대로 유지). 원인 진단(7/15 세션: 색인된 페이지로부터 내부링크 0개인 페이지는 예외 없이 미색인)은 계속 유효 — 아직 개선 신호는 안 보이지만 데이터 자체가 fix 이전 시점이라 판단 보류.
- **심각한 문제 2건**: 리디렉션 페이지 1건, 대체 표준태그 페이지 1건 — 둘 다 호스팅 레벨 이슈로 이미 진단 완료(코드 문제 아님), 계속 무시.
- **잘 나가는 페이지** (position 기준, 7/17까지 확인, 실제 GSC export로 재검증):
  - `car-loan-calculator.html` — 4.07위 (노출 15)
  - `road-trip-cost-calculator.html` — 9.53위 (노출 17)
  - `car-down-payment-calculator.html` — 7.75위 (노출 4, 표본 작음)
  - `/` (홈페이지) — 12.06위 (노출 35)
  - `how-to-check-car-history-before-buying.html` — 9.6위 (노출 5, 표본 작음)
  - **`how-much-car-can-i-afford.html` — 19.39위, 노출 110회로 사이트 전체에서 가장 많음.** "car affordability rules of thumb 2026" 단일 쿼리가 노출 11회에 **3.64위**, "car affordability calculator rules of thumb 2026"은 노출 6회에 **2.17위** — 확인된 사이트 최고 성과 클러스터. **7/19 세션에서 Quick answer 콜아웃 보강 완료**(20/4/10 규칙 + $5,000/월→$500 상한 예시, 기존 highlight-box 예시 수치 그대로 인용). 효과는 다음 GSC 확인(7/22 이후) 때 볼 것.
  - `what-is-good-interest-rate-car-loan.html` — 19.16위 (노출 19). "excellent/good/strong credit 2026" 계열 쿼리 7개가 여전히 17~20위대(예: average auto loan rates excellent credit 2026 노출2/20위, best car loan rates 2026 strong credit 노출1/17위). **7/17-1차 보강이 이 데이터 컷오프(7/17)와 같은 날 나가서 "보강 이후" 데이터가 사실상 0일치 — 아직 효과 판단 불가, 성급하게 추가로 손대지 말 것.**
  - `how-to-negotiate-car-price-at-dealership.html` — 47.17위로 하락(7/12 확인 27.5위 대비) — 표본 12회로 여전히 작음, 성급한 대응 금지(rule 6). 오늘 세션에 Quick answer 보강했으니 다음 확인 때 같이 볼 것.
- **의도적으로 방치 중인 영역**: `car-insurance-estimator.html`(노출 1,074회, 사이트 전체 1위 노출량, 하지만 85.91위)를 포함한 **보험 계열 키워드 전체**. NerdWallet/Progressive/GEICO/Allstate 등이 74~100위권을 완전히 독점 중(쿼리 367개 중 절반 이상이 보험 관련, 전부 저순위). 추가 투자 무의미, 확인된 정책 계속 유지.
- **콘텐츠는 완벽한데 권위도 부족으로 순위가 안 나오는 케이스**: `how-to-get-pre-approved-car-loan.html` (2,313단어, 노출 61회로 준수하지만 77.1위). 신용조합/은행급 대형 사이트가 장악한 영역이라 콘텐츠 보강으로는 해결 안 됨 — 손대지 않기로 결론 유지.
- **표본이 너무 작아 판단 보류 중인 쿼리**: `car refinance pre approval`(노출 3, 3.33위) — 여전히 액션 불가 수준.
- **7/6·7/10·7/17·7/19에 게시된 신규 콘텐츠 전체(negative equity/LTV/bi-weekly/cash-vs-finance/Selling 5종/Glossary/0% APR 2종/lease buyout)**: **페이지 리포트(노출 상위 16개) 어디에도 안 뜸 = 노출 0.** Coverage 데이터가 7/10 컷오프라 이 중 상당수(7/17, 7/19 게시분)는 크롤링 자체가 안 됐을 가능성 높음 — 정상, 1~2주 후 재확인 필요. **7/6·7/10 게시분(negative equity 등)은 이제 게시 후 2주 이상 지났는데도 노출 0 — 슬슬 "왜 아직도 크롤링이 안 됐는지" 색인 정체 이슈와 묶어서 다음 색인 데이터 확인 시 같이 볼 것.**
- **국가별**: 미국이 노출의 90%(1,610/1,835) 차지, 정상. 한국 9회 노출에 1.11위로 튀는 값이 있으나 표본 너무 작아 무의미.
- **기기별**: 데스크톱 1,201 vs 모바일 520 — 노출 비중은 데스크톱이 더 크지만 순위는 모바일이 약간 더 좋음(71.63위 vs 78.06위), 특별한 액션 불필요.

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

## 8. 외부 채널 (변경 없음, 6/29 시점 기준)
- 25개 사이트 등록 완료, footer 뱃지 6개 (NewTool, FoundrList, Fazier, Findly.tools, twelve.tools, PitchWall)
- **사용자가 총 11개 사이트를 운영 중** (autocalchub 포함). 필요시 본인 소유 다른 사이트에서 autocalchub로 상호링크 가능 — 7/15 세션에서 언급됨, **아직 착수 안 함, 지금 우선순위 아니라고 사용자가 명시적으로 보류함**. 다음에 백링크 관련 작업할 때 이 옵션 먼저 검토할 것. 단, 진행 시 유의점: (1) 상호링크가 명백히 기계적/전면적이면 Google 링크 스킴으로 인식될 리스크 있음 — 문맥상 자연스러운 곳에만 소량으로. (2) 나머지 10개 사이트가 뭔지, 주제가 얼마나 관련 있는지 다음 세션에서 먼저 파악 필요(사용자에게 목록 요청).

## 9. GitHub 작업 방식 안내 (신규 세션 시작 시 참고)
- 이 저장소는 사용자가 매 세션 GitHub Personal Access Token을 직접 발급해서 대화 중에 전달하는 방식으로 운영됨. 토큰이 없으면 clone은 되지만(public repo) push는 불가.
- 작업 시작 시: `git clone` → `git remote set-url origin https://<username>:<token>@github.com/canghun13/autocalchub.git` → `git config user.email/name` → `git pull`로 최신화 후 작업.
- 작업은 사용자가 명시적으로 지시했을 때만 진행 (규칙 1). 신규 콘텐츠는 방향 보고 후 승인받고 작성 시작 (규칙 4).
- 완료 후 커밋 메시지에 변경 이유와 근거(경쟁 강도 확인 결과, 어떤 GSC 신호 때문인지 등)를 상세히 남길 것 — 다음 세션에서 이 로그가 유일한 판단 근거가 됨.
