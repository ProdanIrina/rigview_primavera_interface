import { useState } from "react"
import { Button } from "@/components/ui/button"
import LogTable from "@/components/LogTable"
import { useNavigate } from "react-router-dom"

function Dashboard() {
  const navigate = useNavigate()
  const [activities, setActivities] = useState([])
  const [loading, setLoading] = useState(false)
  const [message, setMessage] = useState(null)

  const handleSync = async () => {
    setLoading(true)
    setMessage(null)

    try {
      const response = await fetch("http://localhost:8000/sync/activities")
      if (!response.ok) throw new Error("Eroare la sincronizare")

      const data = await response.json()
      setActivities(data)
      setMessage(`✅ ${data.length} activități sincronizate.`)
    } catch (err) {
      setMessage(`❌ ${err.message}`)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="p-6">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold">Loguri sincronizare</h1>
      </div>

      <Button className="mb-4" onClick={handleSync} disabled={loading}>
        {loading ? "Se sincronizează..." : "Sincronizează acum"}
      </Button>

      {message && <p className="text-sm text-gray-600 mb-4">{message}</p>}

      <LogTable activities={activities} />
    </div>
  )
}

export default Dashboard

