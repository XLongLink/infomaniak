import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Infomaniak SDK for Python',
  description: 'Python SDK documentation for the Infomaniak API.',
  srcDir: 'src',
  base: process.env.NODE_ENV === 'production' ? '/infomaniak/' : '/',
  cleanUrls: true,
  themeConfig: {
    socialLinks: [{ icon: 'github', link: 'https://github.com/XLongLink/infomaniak' }],
    sidebar: [
      { text: 'AI', link: '/ai/', collapsed: true },
      { text: 'Backup', link: '/backup/', collapsed: true, items: [{ text: 'TODO', link: '/backup/' }] },
      { text: 'Cloud', link: '/cloud/', collapsed: true, items: [{ text: 'TODO', link: '/cloud/' }] },
      {
        text: 'Core',
        link: '/core/',
        collapsed: true,
        items: [
          { text: 'TODO', link: '/core/' },
          { text: 'User', link: '/core/user' },
        ],
      },
      { text: 'DNS', link: '/dns/', collapsed: true, items: [{ text: 'TODO', link: '/dns/' }] },
      { text: 'Domain', link: '/domain/', collapsed: true, items: [{ text: 'TODO', link: '/domain/' }] },
      { text: 'kChat', link: '/kchat/', collapsed: true, items: [{ text: 'TODO', link: '/kchat/' }] },
      { text: 'eTickets', link: '/etickets/', collapsed: true, items: [{ text: 'TODO', link: '/etickets/' }] },
      { text: 'kDrive', link: '/kdrive/', collapsed: true, items: [{ text: 'TODO', link: '/kdrive/' }] },
      { text: 'kMeet', link: '/kmeet/', collapsed: true, items: [{ text: 'TODO', link: '/kmeet/' }] },
      { text: 'Mail', link: '/mail/', collapsed: true, items: [{ text: 'TODO', link: '/mail/' }] },
      { text: 'Newsletter', link: '/newsletter/', collapsed: true, items: [{ text: 'TODO', link: '/newsletter/' }] },
      { text: 'Radio', link: '/radio/', collapsed: true, items: [{ text: 'TODO', link: '/radio/' }] },
      { text: 'Tickets', link: '/tickets/', collapsed: true, items: [{ text: 'TODO', link: '/tickets/' }] },
      { text: 'URL', link: '/url/', collapsed: true, items: [{ text: 'TODO', link: '/url/' }] },
      { text: 'Video', link: '/video/', collapsed: true, items: [{ text: 'TODO', link: '/video/' }] },
      { text: 'VOD', link: '/vod/', collapsed: true, items: [{ text: 'TODO', link: '/vod/' }] },
    ],
    search: {
      provider: 'local',
    },
  },
})
