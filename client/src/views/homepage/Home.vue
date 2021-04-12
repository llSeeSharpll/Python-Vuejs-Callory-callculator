<template>
  <div class="container">
    <Callory/>
  </div>
</template>

<script>
// @ is an alias to /src
import Callory from '@/components/Callory'
export default {
  name: 'Home',
  components: {
    Callory
  },
  mounted(){
    if(sessionStorage.getItem('username')==undefined){
      this.$router.push('/login')
    }
  }
}
</script>
