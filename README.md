# Newfact

## I. 메인 페이지 구현   


![image](https://user-images.githubusercontent.com/47061005/99804282-1ac62900-2b7e-11eb-9c87-7ea5987ab81b.png)


<br/>

### *** FragmentMain.java,  fragment_main.xml***

#### 1. 일반 검색   
: **TextEdit**의 값을 넘겨주어 상호명 또는 메뉴명으로 검색을 가능하게 한다.

#### 2. 설정 검색    
![image](https://user-images.githubusercontent.com/47061005/99806718-c7ee7080-2b81-11eb-9dbb-41a65f21f08b.png)

: **SeekBar**를 이용하여 필터를 생성해 성분과 관련해 제한된 값을 조정하고 검색할 수 있도록 한다.

#### 3. 맞춤 메뉴 추천   
: **Firebase**에 접근하여 사용자의 정보와 음료들의 정보를 비교하여 사용자가 설정한 기준치를 넘지 않는   
적절한 음료를 3개 가져와 **RecyclerView**에 담는다.



## II. 상세 정보 페이지 구현
![image](https://user-images.githubusercontent.com/47061005/99805550-16027480-2b80-11eb-86b0-37097b2906e2.png)
![image](https://user-images.githubusercontent.com/47061005/99805601-231f6380-2b80-11eb-88a6-bd186cd790f2.png)

<br/>

### *** ProductDetailPage.java***

#### 1.  상품 상세 정보  
: 상품 상세 설명 페이지에서는 상품과 관련된 정보로 
1)섭취 주의 마크, 2)상품 상세 정보, 3)영양 성분 제공, 4) 알레르기 정보 표시를 보여줍니다.
**Firebase**에 접근하여 음료들의 정보를 가져와 이미지, 메뉴명, 프렌차이즈명, 상품설명, 성분함량, 알레르기정보를 보여줍니다.   

![image](https://user-images.githubusercontent.com/47061005/99805437-e6536c80-2b7f-11eb-8ed3-5449398ae66c.png)
![image](https://user-images.githubusercontent.com/47061005/99806180-f881da80-2b80-11eb-9b72-441ce5731480.png)


#### 2.  필터링 정보 반영 
![image](https://user-images.githubusercontent.com/47061005/99806555-83fb6b80-2b81-11eb-9763-e9edde2c0b38.png)

: **Firebase**에 접근하여 사용자의 정보와 음료들의 정보를 비교하여 사용자가 설정한 기준치를 넘거나 
주의해야하는 알레르기 성분이 담긴 음료가 있다면 각각의 notice마크를 상단에 띄운다.
