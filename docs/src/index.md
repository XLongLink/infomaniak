---
layout: false
---

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vitepress'

const router = useRouter()

onMounted(() => {
  router.go('/markdown-examples')
})
</script>

<meta http-equiv="refresh" content="0; url=/markdown-examples">
<link rel="canonical" href="/markdown-examples">
