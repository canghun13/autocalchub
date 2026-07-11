# AutoCalcHub 인수인계 문서 (2026-07-12 기준)

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
- 블로그 44개 (`blog/` 폴더, index.html 제외)
- 툴 21개 (`tools/` 폴더, index.html 제외)
- sitemap.xml 총 URL 71개 (블로그+툴+정적페이지+blog/index+tools/index)
- `tools/index.html` — 블로그 인덱스와 동일한 구조(카테고리별 그리드 + 검색기능)로 신규 생성됨 (기존엔 없었음)

### 사이트 구조 관련 중요 변경사항
- **헤더 내비게이션**: 기존 "Calculators"/"Blog" 드롭다운 메뉴 → **단순 링크**로 전환. "Calculators" 명칭도 **"Tools"**로 변경됨. (`assets/partials/header.html`)
- **"← All tools" 백링크**: `assets/js/components.js`에서 관리, `tools/index.html`로 연결됨 (예전엔 홈페이지 `#tools` 앵커였는데 수정함). 툴 목록 페이지 자체에서는 이 링크가 안 뜨도록 처리돼 있음.
- 모든 페이지는 `assets/partials/header.html`, `footer.html`을 JS(`components.js`)로 fetch해서 공유 렌더링 — 헤더/푸터는 한 곳만 고치면 전체 사이트에 반영됨.

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

## 4. 주간 루틴 (정기 작업, 일요일)
- 매주 일요일: 블로그 3개 + 툴 1개 **신규 또는 보강**
- 작업 시작 전 GA4 + Search Console 리포트 캡처 받아서 방향 잡기
- **정기 루틴과 별개로**, 세션 여유가 있을 때 GSC 데이터 기반 추가 보강/신규 작업을 하기도 함 (7/8, 7/10 세션이 이 케이스) — 이건 "주간 루틴 소진"과 무관하게 별도로 카운트됨

## 5. SEO / Search Console 현황 (2026-07-12 기준 최신 확인)
- **노출수**: 5/14~5/20에 하루 200~270회로 급증(보험 키워드 초기 크롤링 테스트성 노출) → 5/21 이후 하루 0~4회로 7주째 유지 중. 이게 지금의 진짜 baseline이며 정상적인 저권위 신규 도메인 패턴으로 판단 중.
- **클릭수**: 3개월 누적 **0건**. 표본이 워낙 작아서(대부분 페이지 노출 4~110회) 통계적으로 이상 신호 아님.
- **색인 현황**: Coverage 리포트는 항상 1~2주 지연 반영됨(예: 7/12에 받은 리포트가 6/30 데이터까지만 있음) — 최신 작업 반영 여부 확인 시 이 지연을 감안할 것.
- **색인 생성됨**: 과거 스냅샷 기준 16개, "발견됨-크롤링대기" 45개, "크롤링됨-미생성" 2개였음 (7/12 리포트 기준, 최신 반영 전).
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

### 7/12 세션: GSC 데이터 재확인, 작업 없음으로 결론
- Performance + Coverage 리포트 확인. Coverage는 6/30 데이터까지만 반영(지연), Performance는 7/10 세션과 거의 동일한 패턴(노출 여전히 하루 0~4건, 신규 콘텐츠는 아직 노출 0건 — 정상적으로 너무 이름)
- **신규 이슈 2건 조사**: "리디렉션 포함 페이지(실패함)" 1건, "적절한 표준 태그 대체 페이지" 1건 → 코드 전체 검증(http:// 하드코딩, www. 절대경로, 잘못된 canonical) 결과 전부 없음 확인 → **호스팅 레벨(Cloudflare/GitHub Pages)의 정상적인 http→https 리디렉션으로 판단, 코드 수정 불필요**
- 수익화(AdSense) 관점에서 냉정하게 판단: 3개월 누적 클릭 0건인 상황에서 신규 콘텐츠를 더 만들어도 단기 매출 영향 없음 → **오늘은 작업 없음으로 결론**, 억지로 일 만들지 않음

## 7. 다음 작업 후보 (아직 미착수)
- negative-equity/LTV/bi-weekly 클러스터(7/6·7/10 게시)의 색인·노출 여부 1~2주 후 재확인 필요
- 색인 생성 수가 7/6~7/10 보강분 이후 실제로 늘었는지 Coverage 리포트로 확인 (지연 감안, 최소 2주 후)
- `how-to-get-pre-approved-car-loan.html`처럼 "콘텐츠는 완벽한데 권위도 때문에 순위 안 나오는" 페이지들은 콘텐츠 작업 대신 **백링크/외부 채널 확대**가 근본 해법일 가능성 — 아직 미착수 영역

## 8. 외부 채널 (변경 없음, 6/29 시점 기준)
- 25개 사이트 등록 완료, footer 뱃지 6개 (NewTool, FoundrList, Fazier, Findly.tools, twelve.tools, PitchWall)

## 9. GitHub 작업 방식 안내 (신규 세션 시작 시 참고)
- 이 저장소는 사용자가 매 세션 GitHub Personal Access Token을 직접 발급해서 대화 중에 전달하는 방식으로 운영됨. 토큰이 없으면 clone은 되지만(public repo) push는 불가.
- 작업 시작 시: `git clone` → `git remote set-url origin https://<username>:<token>@github.com/canghun13/autocalchub.git` → `git config user.email/name` → `git pull`로 최신화 후 작업.
- 작업은 사용자가 명시적으로 지시했을 때만 진행 (규칙 1). 신규 콘텐츠는 방향 보고 후 승인받고 작성 시작 (규칙 4).
- 완료 후 커밋 메시지에 변경 이유와 근거(경쟁 강도 확인 결과, 어떤 GSC 신호 때문인지 등)를 상세히 남길 것 — 다음 세션에서 이 로그가 유일한 판단 근거가 됨.
