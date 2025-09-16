import { render, screen } from '@testing-library/react'
import '@testing-library/jest-dom'
import HomePage from '../src/app/page'

describe('Home Page', () => {
  it('renders the main heading', () => {
    render(<HomePage />)
    
    const heading = screen.getByRole('heading', {
      name: /AI-Powered SAP Migration Platform/i,
    })
    
    expect(heading).toBeInTheDocument()
  })

  it('renders the get started button', () => {
    render(<HomePage />)
    
    const button = screen.getByRole('link', { name: /get started/i })
    
    expect(button).toBeInTheDocument()
    expect(button).toHaveAttribute('href', '/dashboard')
  })

  it('renders the view demo button', () => {
    render(<HomePage />)
    
    const button = screen.getByRole('link', { name: /view demo/i })
    
    expect(button).toBeInTheDocument()
    expect(button).toHaveAttribute('href', '/demo')
  })
})
