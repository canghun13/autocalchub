# AutoCalcHub 인수인계 문서 (2026-07-17 기준)

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

## 5. SEO / Search Console 현황 (2026-07-15 기준 최신 확인)
- **노출수**: 5/14~5/20에 하루 200~270회로 급증(보험 키워드 초기 크롤링 테스트성 노출) → 5/21 이후 하루 0~4회로 7주째 유지 중. 이게 지금의 진짜 baseline이며 정상적인 저권위 신규 도메인 패턴으로 판단 중.
- **클릭수**: 3개월 누적 **0건**. 표본이 워낙 작아서(대부분 페이지 노출 4~110회) 통계적으로 이상 신호 아님.
- **색인 현황**: Coverage 리포트는 항상 1~2주 지연 반영됨(예: 7/12에 받은 리포트가 6/30 데이터까지만 있음) — 최신 작업 반영 여부 확인 시 이 지연을 감안할 것.
- **색인 생성됨**: 16개로 6월 초 이후 정체, "발견됨-크롤링대기" 53개 + "크롤링됨-미생성" 2개 = 미색인 55개 (7/15 리포트 기준, 7/12 대비 오히려 47→55로 증가). **원인 진단 완료(7/15 세션)**: 색인된 페이지로부터 내부링크를 0개 받는 페이지는 예외 없이 전부 미색인 — 자세한 내용은 7/15 세션 로그 참고.
- **잘 나가는 페이지** (position 기준, 7/12 확인):
  - `car-loan-calculator.html` — 4.07위
  - `road-trip-cost-calculator.html` — 7.44위
  - `car-down-payment-calculator.html` — 7.75위
  - `/` (홈페이지) — 12.06위
  - `how-to-check-car-history-before-buying.html` — 9.6위
  - `how-much-car-can-i-afford.html` — 19.39위 (특정 "rules of thumb 2026" 키워드는 2~6위까지 나옴, 사이트 최고 성과 페이지)
  - `what-is-good-interest-rate-car-loan.html` — 19.16위 ("auto loan rates 2026 by credit tier" 계열에서 17~20위)
  - `how-to-negotiate-car-price-at-dealership.html` — 27.5위
- **의도적으로 방치 중인 영역**: `car-insurance-estimator.html`(노출 1위, 1,074회)를 포함한 **보험 계열 키워드 전체**. NerdWallet/Progressive/GEICO/Allstate 등이 80~95위권을 완전히 독점 중이라 추가 투자 무의미. 확인된 정책, 계속 유지.
- **콘텐츠는 완벽한데 권위도 부족으로 순위가 안 나오는 케이스**: `how-to-get-pre-approved-car-loan.html` (2,313단어, Related Guides·내부링크 8개 유입 다 있는데 79.6위). 신용조합/은행급 대형 사이트가 장악한 영역이라 콘텐츠 보강으로는 해결 안 됨 — 손대지 않기로 결론.
- **신규 콘텐츠(negative equity/LTV/bi-weekly, 7/6·7/10 게시)**: 7/12 기준 노출 0건. 너무 최근이라 정상, 1~2주 후 재확인 필요.
- **롱테일 금리 쿼리 클러스터 (7/17 발견, 보강 완료)**: "best/average car loan rates 2026 (excellent/good/strong credit)" 계열 7개 쿼리가 17~20위에 몰려있던 것 확인 → `what-is-good-interest-rate-car-loan.html` Q1 2026 데이터로 갱신 + 검색어 실사용 표현 병기로 대응. 효과는 다음 세션 이후 확인.
- **신규 페이지 (7/17 2차 게시)**: `blog/should-you-pay-cash-or-finance-a-car.html` — "현금 vs 대출" 갭 콘텐츠. 노출/색인 여부 다음 세션 이후 확인 필요.

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

## 7. E-E-A-T 관련 향후 후보 (미착수)
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
