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
      { text: 'AI', link: '/ai/', collapsed: true, items: [{ text: 'TODO', link: '/ai/todo' }] },
      { text: 'Backup', link: '/backup/', collapsed: true, items: [{ text: 'TODO', link: '/backup/todo' }] },
      {
        text: 'Cloud',
        link: '/cloud/',
        collapsed: true,
        items: [
          { text: 'TODO', link: '/cloud/todo' },
          {
            text: 'Kubernetes',
            collapsed: true,
            items: [{ text: 'Data', link: '/cloud/kubernetes/data' }],
          },
        ],
      },
      {
        text: 'Core',
        link: '/core/',
        collapsed: true,
        items: [
          { text: 'TODO', link: '/core/todo' },
          { text: 'User', link: '/core/user' },
        ],
      },
      { text: 'DNS', link: '/dns/', collapsed: true, items: [{ text: 'TODO', link: '/dns/todo' }] },
      { text: 'Domain', link: '/domain/', collapsed: true, items: [{ text: 'TODO', link: '/domain/todo' }] },
      {
        text: 'eTickets',
        link: '/etickets/',
        collapsed: true,
        items: [{ text: 'TODO', link: '/etickets/todo' }],
      },
      { text: 'kChat', link: '/kchat/', collapsed: true, items: [{ text: 'TODO', link: '/kchat/todo' }] },
      { text: 'kDrive', link: '/kdrive/', collapsed: true, items: [{ text: 'TODO', link: '/kdrive/todo' }] },
      { text: 'kMeet', link: '/kmeet/', collapsed: true, items: [{ text: 'TODO', link: '/kmeet/todo' }] },
      { text: 'Mail', link: '/mail/', collapsed: true, items: [{ text: 'TODO', link: '/mail/todo' }] },
      {
        text: 'Newsletter',
        link: '/newsletter/',
        collapsed: true,
        items: [{ text: 'TODO', link: '/newsletter/todo' }],
      },
      { text: 'Radio', link: '/radio/', collapsed: true, items: [{ text: 'TODO', link: '/radio/todo' }] },
      { text: 'Tickets', link: '/tickets/', collapsed: true, items: [{ text: 'TODO', link: '/tickets/todo' }] },
      { text: 'URL', link: '/url/', collapsed: true, items: [{ text: 'TODO', link: '/url/todo' }] },
      { text: 'Video', link: '/video/', collapsed: true, items: [{ text: 'TODO', link: '/video/todo' }] },
      { text: 'VOD', link: '/vod/', collapsed: true, items: [{ text: 'TODO', link: '/vod/todo' }] },
    ],
    search: {
      provider: 'local',
    },
  },
})
