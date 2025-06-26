import { Link } from "react-router-dom"

export default function Navbar() {
  return (
    <nav className="bg-primary text-black px-6 py-3 shadow-md flex justify-between">
      <h1 className="text-xl font-bold">RigView Interface</h1>
      <div className="flex gap-4">
        <Link to="/" className="hover:underline">Dashboard</Link>
        <Link to="/credentials" className="hover:underline">Credentiale</Link>
      </div>
    </nav>
  )
}
