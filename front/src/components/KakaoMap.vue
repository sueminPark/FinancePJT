<template>
    <div id="map" style="width:600px;height:500px;margin-left: auto;margin-right: auto;"></div>
    <br>
    <div>
        <label for="category">은행 : </label>
            <select v-model="selectedCategory1" id="category" class="form-select; center" aria-label="Default select example" style="width:200px;height:50px;" required>
                <option value="" disabled selected>다음 중 하나를 선택하세요.</option>
                <option v-for="bank in banks" v-bind:key="bank.id" :value="bank">{{ bank.name }}</option>
            </select>
            
            <!--키워드 검색 칸-->
            <input
            type="text"
            id="keyword"
            v-model="keyword"
            />  <button type="button" class="btn btn-dark" @click="loadScript">검색</button>    
            
    </div>   
</template>


<script setup>
import { onMounted, ref } from 'vue';

let map = null;
const keyword = ref(null)

const selectedCategory1 = ref('')
// const markers = ref([])


const loadScript = () => {
    result = selectedCategory1.value.name + keyword.value
    // console.log('result', result)
    // console.log("selectedCategory1", selectedCategory1.value)

    const key = import.meta.env.VITE_KAKAO_API_KEY
    const script = document.createElement('script')

    script.onload = () => kakao.maps.load(startPoint)
    script.src = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${key}&libraries=services`
    document.head.appendChild(script)
    // const infowindow = new kakao.maps.InfoWindow({zindex:1});
}

onMounted(() => {
    if (window.kakao?.maps) {
        console.log(`KakaoMap.vue - 이미 map 있음`, window.kakao.maps)
    } else {
        console.log(`KakaoMap.vue - map script loading 필요`)
        loadScript()
    }
})

const startPoint = () => {
    const infowindow = new kakao.maps.InfoWindow({zindex:1});
    // 헷갈렸던 포인트 *** -> container를 내부에 써줘야함
    const container = document.getElementById('map')
    
    const options = {
        center: new kakao.maps.LatLng(33.450701, 126.570667),
        level: 3 
    }
    map = new kakao.maps.Map(container, options)
    
    const displayMarker = (place) => {
        const marker = new kakao.maps.Marker({
            map: map,
            position: new kakao.maps.LatLng(place.y, place.x)
        });    

        kakao.maps.event.addListener(marker, 'click', function() {
            infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
            infowindow.open(map, marker);
        });    
    }

    const placesSearchCB = (data, status) => {
        if (status === kakao.maps.services.Status.OK) {
            const bounds = new kakao.maps.LatLngBounds();

            for (let i=0; i < data.length; i++) {
                displayMarker(data[i]);
                bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
            }    
            // 검색된 장소 위치를 기준으로 지도 범위 재설정
            map.setBounds(bounds);
        }
    } 

    const ps = new kakao.maps.services.Places();

    console.log(result)
    ps.keywordSearch(result, placesSearchCB);
    // console.log(keyword.value)
    
};


let result = ''
const banks = ref([
    { name: '국민은행', value: '국민은행' },    
    { name: '우리은행', value: '우리은행' },
    { name: '신한은행', value: '신한은행' },
    { name: 'KEB하나은행', value: 'KEB하나은행' },
    { name: '기업은행', value: '기업은행' },
    { name: '하나은행', value: '하나은행' },
    { name: '외환은행', value: '외환은행' },
    { name: '수협은행', value: '수협은행' },
    { name: '신협중앙회', value: '신협중앙회' },
    { name: '한국씨티은행', value: '한국씨티은행' }
]) 
    
</script>


<style scoped>
.center {
    text-align: center;
}
</style>