<h5 id="들어가며">들어가며</h5>
<p>(주의!) 너무너무 졸려서 정신줄 놓고 작성하는 TIL입니다. 
<del>타인이 읽을 것을 전혀 가정하지 않은 채 작성되었습니다. 일단 대강 써두고 나중에 내용을 추가할 예정이라 다시보실때는 내용이 달라질 수 있음에 유의하시기 바랍니다.</del> </p>
<h2 id="문제">문제</h2>
<p><a href="https://www.acmicpc.net/problem/1654">백준1654 - 랜선 자르기</a>
<img alt="랜선 자르기" src="https://velog.velcdn.com/images/edocnuyh/post/19504691-de3d-49ee-ad68-5bf8c4a65763/image.png" /></p>
<br />


<h2 id="뭘-물어보는-걸까">뭘 물어보는 걸까?</h2>
<p>오늘도 나는 문제를 보면서 까만건 글씨요, 하얀건 화면이구나.. 이러면서 쳐다보기만 한다. 머릿속은 온통 '어쩌라고..?'로만 가득해..
<img alt="졸리고 이해못하는 나" src="https://velog.velcdn.com/images/edocnuyh/post/7850513b-7dd1-463a-b501-3670590bc84b/image.png" /></p>
<p>결국 다시 또 백준님의 힌트를 봄.
<img alt="매개~변수~탐색~" src="https://velog.velcdn.com/images/edocnuyh/post/81d0a8b7-cbbe-4e29-ad8c-63667cb0300e/image.png" /></p>
<h3 id="매개-변수-탐색">매개 변수 탐색</h3>
<p>그리고 맞닥뜨린 <strong>매개 변수 탐색</strong>.. 넌 누구니 전혀 처음 들어보는구나. 이름으로는 전혀 유추를 할수가 없어.. 그래서 조신히 검색을 갈김.</p>
<p><a href="https://annajeong.github.io/algorithm/parametric/">참고블로그1 - 이진 탐색 &amp; 매개 변수 탐색</a>
위 블로그에 정리가 잘 되어있다. 내 식으로 정리하는 건 추후에..
이진탐색과 유사하게 동작하지만, 범위를 한 방향으로 좁히는 것이 아닌 널뛰기를 하면서 좁히는 느낌.
결국은 답이 될 수 있는 여러 값들 중 최솟값, 최댓값을 구하는 느낌이다..</p>
<h3 id="upper-bound-lower-bound">Upper Bound, Lower Bound</h3>
<h4 id="-upper-bound----최댓값">[ Upper Bound ] - 최댓값</h4>
<h4 id="-lower-bound----최솟값">[ Lower Bound ] - 최솟값</h4>
<br />

<h2 id="고난">고난</h2>
<p>살려주세요 살려주세요 머리가 돌아가지 않아요. 저는 자꾸 틀리고 있어요.
결국 검색으로 극복(?)함.. </p>
<p><a href="https://st-lab.tistory.com/269">참고블로그2</a></p>
<p>기존에 나는 아래와 같은 방식으로 탐색을 하고 있었다.</p>
<pre><code class="language-java">    long start = 1; 
    long end = max;
       long mid = 0;

    while (start &lt; end) {
        mid = (end + start) / 2;

        long count = 0;
        for (int i = 0; i &lt; arr.length; i++) {
            count += arr[i] / mid; // 위험!!
        }
        if (count &gt;= N) {
            start = mid + 1;
        } else {
            end = mid;
        }
    }</code></pre>
<p>랜선을 0cm로 자르진 않을거니까 <code>start</code>를 1로 두고, <code>end</code>는 주어진 랜선길이 중 가장 큰 수로 두었다.
그런데 코드 중간에 보면 나눗셈을 <code>mid</code>라는 변수로 하고 있는데, 이 변수가 0이 될 가능성이 있다는 것을 전혀 눈치채지 못하고 있어 자꾸만 <strong>틀렸습니다!</strong>의 늪에 빠져있던 것이다..</p>
<p>그렇다면 <code>mid</code>의 값이 0이 되지 못하게 하려면? <code>end = max + 1</code>로 범위를 설정하여주면 된다고 위 참고블로그에서 설명해주시고 있다.. 그래서 그렇게 따라함(관련 내용은 추후 정리..)</p>
<p>근데 이제 보니 내 코드는 start값을 1로 주어서 max가 1인 경우 <code>start = 1 = end</code> 이렇게 되어버려 반복문이 작동하지 않고, <code>start - 1 = 0</code>을 출력해서 계속 틀렸던거 같다. </p>
<p>어쨋든 <strong>나누기 0</strong>은 유의하면 좋으니까 오늘 한번더 가슴에 새겨두자.</p>
<h3 id="최종제출코드">최종제출코드</h3>
<pre><code class="language-java">public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int K = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        long[] arr = new long[K];
        arr[0] =  Long.parseLong(br.readLine());
        long max = arr[0];
        for (int i = 1; i &lt; K; i++) {
            arr[i] = Long.parseLong(br.readLine());
            if (arr[i] &gt; max){
                max = arr[i];
            }
        }


        long start = 1;
        long end = max + 1;
        long mid = 0;

        while (start &lt; end) {
            mid = (end + start) / 2;

            long count = 0;
            for (int i = 0; i &lt; arr.length; i++) {
                count += arr[i] / mid;
            }
            if (count &gt;= N) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }

        System.out.println(start - 1);
    }
}</code></pre>
<br />

<h2 id="정리">정리</h2>
<ul>
<li>시간이 많을 때 미리미리 공부해둘 걸 후회하는 중.</li>
<li><strong>매개 변수 탐색</strong> : 널뛰기 탐색</li>
<li><strong>Upper Bound, Lower Bound</strong> : 최댓값 최솟값</li>
<li><strong><code>숫자 / 0</code></strong> 이 되지않도록 주의하자!!!! </li>
</ul>