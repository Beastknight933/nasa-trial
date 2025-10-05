import { Home, Search, Compass, Cpu, Info } from 'lucide-react';

export default function HomePage() {
  return (
    <div className="min-h-screen bg-black text-white flex">
      {/* Sidebar */}
      <aside className="w-64 bg-gradient-to-b from-gray-900 to-black border-r border-gray-800 p-6 flex flex-col">
        <div className="mb-8">
          <h1 className="text-xl font-bold">Mandel's Descendents</h1>
        </div>

        <nav className="space-y-2">
          <button className="w-full flex items-center gap-3 px-4 py-3 rounded-lg bg-cyan-500 text-white font-medium">
            <Home size={20} />
            <span>Home</span>
          </button>

          <button className="w-full flex items-center gap-3 px-4 py-3 rounded-lg text-gray-300 hover:bg-gray-800 transition-colors">
            <Search size={20} />
            <span>Research</span>
          </button>

          <button className="w-full flex items-center gap-3 px-4 py-3 rounded-lg text-gray-300 hover:bg-gray-800 transition-colors">
            <Compass size={20} />
            <span>Discoveries</span>
          </button>

          <button className="w-full flex items-center gap-3 px-4 py-3 rounded-lg text-gray-300 hover:bg-gray-800 transition-colors">
            <Cpu size={20} />
            <span>AI Query</span>
          </button>

          <button className="w-full flex items-center gap-3 px-4 py-3 rounded-lg text-gray-300 hover:bg-gray-800 transition-colors">
            <Info size={20} />
            <span>About</span>
          </button>
        </nav>
      </aside>

      {/* Main Content */}
      <main className="flex-1 relative overflow-hidden">
        {/* Background Image */}
        <div
          className="absolute inset-0 bg-cover bg-center opacity-40"
          style={{ backgroundImage: 'url(/earth.png)' }}
        />

        {/* Content Overlay */}
        <div className="relative z-10 px-16 py-12">
          {/* Hero Section */}
          <div className="text-center mb-12">
            <h1 className="text-6xl font-bold mb-4">
              Unlocking the Secrets of Space Biology
            </h1>
            <p className="text-xl text-gray-300 mb-8">
              Search. Learn. Discover the unknown.
            </p>

            {/* Search Bar */}
            <div className="max-w-3xl mx-auto flex gap-2">
              <input
                type="text"
                placeholder="Search for space biology research"
                className="flex-1 px-6 py-4 rounded-full bg-gray-900/80 border border-gray-700 text-white placeholder-gray-400 focus:outline-none focus:border-cyan-500 transition-colors backdrop-blur-sm"
              />
              <button className="px-8 py-4 rounded-full bg-cyan-500 text-white font-semibold hover:bg-cyan-600 transition-colors">
                Search
              </button>
            </div>
          </div>

          {/* AI Results Section */}
          <div className="mt-16">
            <h2 className="text-3xl font-bold mb-8">AI Results</h2>
            <div className="space-y-6 max-w-7xl">
              {/* Card 1 */}
              <div className="bg-gray-900/60 backdrop-blur-md rounded-2xl p-6 border border-gray-800 hover:border-gray-700 transition-colors flex items-center gap-6">
                <div className="w-64 h-40 bg-gradient-to-br from-gray-800 to-gray-900 rounded-xl flex-shrink-0 overflow-hidden">
                  <img
                    src="https://images.pexels.com/photos/2280571/pexels-photo-2280571.jpeg?auto=compress&cs=tinysrgb&w=800"
                    alt="Space Biology"
                    className="w-full h-full object-cover"
                  />
                </div>
                <div>
                  <h3 className="text-xl font-bold mb-2">
                    AI-Powered Space Biology Search Engine
                  </h3>
                  <p className="text-gray-400">
                    Explore the vast universe of space biology with our AI-driven search engine. Discover groundbreaking research, innovative discoveries, and the latest advancements in the field.
                  </p>
                </div>
              </div>

              {/* Card 2 */}
              <div className="bg-gradient-to-br from-teal-600/40 to-teal-800/40 backdrop-blur-md rounded-2xl p-6 border border-teal-700/50 hover:border-teal-600/50 transition-colors flex items-center gap-6">
                <div className="w-64 h-40 bg-gradient-to-br from-teal-500 to-teal-700 rounded-xl flex-shrink-0 flex items-center justify-center">
                  <div className="text-center space-y-4">
                    <div className="w-24 h-8 bg-white rounded-t-full mx-auto"></div>
                    <div className="space-y-2">
                      <div className="w-16 h-16 bg-white rounded-full mx-auto"></div>
                      <div className="w-12 h-3 bg-white/80 rounded-full mx-auto"></div>
                      <div className="w-10 h-3 bg-white/60 rounded-full mx-auto"></div>
                    </div>
                  </div>
                </div>
                <div>
                  <h3 className="text-xl font-bold mb-2">
                    Uncover the Mysteries of Space Biology
                  </h3>
                  <p className="text-gray-200">
                    Delve into the fascinating world of space biology and uncover the secrets of life beyond Earth. Our search engine provides access to a wealth of knowledge.
                  </p>
                </div>
              </div>

              {/* Card 3 */}
              <div className="bg-gray-900/60 backdrop-blur-md rounded-2xl p-6 border border-gray-800 hover:border-gray-700 transition-colors flex items-center gap-6">
                <div className="w-64 h-40 bg-gradient-to-br from-teal-900 to-teal-950 rounded-xl flex-shrink-0 overflow-hidden">
                  <img
                    src="https://images.pexels.com/photos/1072179/pexels-photo-1072179.jpeg?auto=compress&cs=tinysrgb&w=800"
                    alt="Plant Biology"
                    className="w-full h-full object-cover"
                  />
                </div>
                <div>
                  <h3 className="text-xl font-bold mb-2">
                    Discover the Latest Space Biology Discoveries
                  </h3>
                  <p className="text-gray-400">
                    Stay up-to-date with the latest discoveries in space biology. Our search engine aggregates information from leading research institutions and space agencies.
                  </p>
                </div>
              </div>
            </div>
          </div>
        
          {/* Footer */}
          <footer className="mt-16 py-6 text-center text-gray-400 border-t border-gray-800">
            <p>© 2025 Mandel's Descendants. All rights reserved.</p>
          </footer>
          
        </div>
        
      </main>
    </div>
  );
}


