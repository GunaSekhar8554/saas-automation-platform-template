import Link from 'next/link'
import { Button } from '@/components/ui/button'

export default function HomePage() {
  return (
    <div className="flex flex-col min-h-screen">
      {/* Header */}
      <header className="px-4 lg:px-6 h-14 flex items-center border-b">
        <Link className="flex items-center justify-center" href="/">
          <span className="font-bold text-xl">SaaS Platform</span>
        </Link>
        <nav className="ml-auto flex gap-4 sm:gap-6">
          <Link
            className="text-sm font-medium hover:underline underline-offset-4"
            href="/features"
          >
            Features
          </Link>
          <Link
            className="text-sm font-medium hover:underline underline-offset-4"
            href="/pricing"
          >
            Pricing
          </Link>
          <Link
            className="text-sm font-medium hover:underline underline-offset-4"
            href="/docs"
          >
            Docs
          </Link>
        </nav>
      </header>

      {/* Main Content */}
      <main className="flex-1">
        <section className="w-full py-12 md:py-24 lg:py-32 xl:py-48">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center space-y-4 text-center">
              <div className="space-y-2">
                <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl lg:text-6xl/none">
                  AI-Powered SAP Migration Platform
                </h1>
                <p className="mx-auto max-w-[700px] text-gray-500 md:text-xl dark:text-gray-400">
                  Automate your PI/PO to SAP BTP Integration Suite migration with intelligent AI agents.
                  Reduce migration time by 80% and eliminate manual errors.
                </p>
              </div>
              <div className="space-x-4">
                <Button asChild>
                  <Link href="/dashboard">Get Started</Link>
                </Button>
                <Button variant="outline" asChild>
                  <Link href="/demo">View Demo</Link>
                </Button>
              </div>
            </div>
          </div>
        </section>

        <section className="w-full py-12 md:py-24 lg:py-32 bg-gray-100 dark:bg-gray-800">
          <div className="container px-4 md:px-6">
            <div className="grid gap-10 sm:px-10 md:gap-16 md:grid-cols-2">
              <div className="space-y-4">
                <h2 className="text-3xl font-bold tracking-tighter md:text-4xl/tight">
                  Intelligent Migration Automation
                </h2>
                <p className="max-w-[600px] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-gray-400">
                  Our AI agents analyze your existing PI/PO integrations, generate migration strategies, 
                  and automatically create BTP Integration Suite artifacts.
                </p>
              </div>
              <div className="space-y-4">
                <h3 className="text-2xl font-bold">Key Features</h3>
                <ul className="space-y-2 text-gray-500 dark:text-gray-400">
                  <li>• Automated code analysis and migration planning</li>
                  <li>• AI-powered artifact generation</li>
                  <li>• Real-time migration monitoring</li>
                  <li>• Multi-tenant SaaS architecture</li>
                  <li>• Enterprise-grade security and compliance</li>
                </ul>
              </div>
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="flex flex-col gap-2 sm:flex-row py-6 w-full shrink-0 items-center px-4 md:px-6 border-t">
        <p className="text-xs text-gray-500 dark:text-gray-400">
          © 2025 SaaS Automation Platform. All rights reserved.
        </p>
        <nav className="sm:ml-auto flex gap-4 sm:gap-6">
          <Link className="text-xs hover:underline underline-offset-4" href="/privacy">
            Privacy
          </Link>
          <Link className="text-xs hover:underline underline-offset-4" href="/terms">
            Terms
          </Link>
        </nav>
      </footer>
    </div>
  )
}
